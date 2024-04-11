import torch
from eraV2Project.utility import modelHelper

import logging
from eraV2Project.common import constant
logger = logging.getLogger(constant.APP_NAME).getChild(__name__)


print_test_result_shape = True
def test_loop(dataloader, model, loss_fn ,max_image_stack = 10):

    device = modelHelper.get_device()
    # Set the model to evaluation mode - important for batch normalization and dropout layers
    # Unnecessary in this situation but added for best practices
    model.eval()
    num_batches = len(dataloader)
    test_loss, correct = 0, 0
    global print_test_result_shape

    correctly_predicted_images = []
    wrongly_predicted_images = []


    # Evaluating the model with torch.no_grad() ensures that no gradients are computed during test mode
    # also serves to reduce unnecessary gradient computations and memory usage for tensors with requires_grad=True    
    
    with torch.no_grad():
        for batch_data, batch_labels in dataloader:
            batch_data, batch_labels = batch_data.to(device), batch_labels.to(device)            
            batch_predictions = model(batch_data)            

            # Print the true indices
            if(print_test_result_shape):
                logger.debug("Test loop parameters shapes")
                modelHelper.print_analysis_shapes(batch_data, batch_labels, batch_predictions)
                print_test_result_shape = False

            argmax_data = batch_predictions.argmax(dim=1)
            true_indices, false_indices = modelHelper.get_true_and_false_indices(batch_predictions, batch_labels)
                

            for image_index in true_indices:
                if(len(correctly_predicted_images) < max_image_stack):
                    selected_image = batch_data[image_index]
                    correctly_predicted_images.append((selected_image, argmax_data[image_index]))

            for image_index in false_indices:
                if(len(wrongly_predicted_images) < max_image_stack):
                    selected_image = batch_data[image_index]
                    wrongly_predicted_images.append((selected_image, argmax_data[image_index]))

            test_loss += loss_fn(batch_predictions, batch_labels).item()
            correct += modelHelper.get_correct_prediction_count(batch_predictions, batch_labels)


    logger.info('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
        test_loss, correct, len(dataloader.dataset),
        100. * correct / len(dataloader.dataset)))
    
    return 100. * correct / len(dataloader.dataset) , test_loss / num_batches, correctly_predicted_images, wrongly_predicted_images