from tqdm import tqdm
from torch import optim
from eraV2Project.utility import modelHelper

import logging
from eraV2Project.common import constant
logger = logging.getLogger(constant.APP_NAME).getChild(__name__)


print_train_result_shape = True
def train_loop(dataloader, model, loss_fn, optimizer : optim.Optimizer, max_image_stack = 10):

    global print_train_result_shape
    device = modelHelper.get_device()
    correctly_predicted_images = []
    wrongly_predicted_images = []

    model.train()
    progressive_batches = tqdm(dataloader)
    
    train_loss = 0
    correct = 0
    processed = 0

    for batch_id, (batch_data, batch_labels) in enumerate(progressive_batches):
        batch_data, batch_labels = batch_data.to(device), batch_labels.to(device)
        # Compute prediction and loss

        optimizer.zero_grad()
        batch_predictions = model(batch_data)
        loss = loss_fn(batch_predictions, batch_labels)
        train_loss+=loss.item()

        # back propagation
        loss.backward()
        optimizer.step()

        if(print_train_result_shape):
            logger.debug("Train loop parameters shapes")
            modelHelper.print_analysis_shapes(batch_data, batch_labels, batch_predictions)
            logger.debug(f"shape of loss: {loss.shape}")
            print_train_result_shape = False

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


        
        correct += modelHelper.get_correct_prediction_count(batch_predictions, batch_labels)
        processed += len(batch_data)
        progressive_batches.set_description(desc= f'Train: Loss={loss.item():0.4f} Batch_id={batch_id} Accuracy={100*correct/processed:0.2f}')


    return 100*correct/processed , train_loss/len(dataloader), correctly_predicted_images, wrongly_predicted_images

