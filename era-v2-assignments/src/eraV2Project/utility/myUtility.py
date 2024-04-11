import random
import torch
import logging
from sampleProject.common import constant

logger = logging.getLogger(constant.APP_NAME).getChild(__name__)

def get_device(use_seed = True):
    is_gpu_available = torch.cuda.is_available()
    
    SEED = 1
    device = "cpu"
    if(is_gpu_available):
        device = "cuda"
        # This ensures that computations involving randomness on the GPU will produce the same results
        # when the seed is the same, even if you run the code multiple times.
        if(use_seed):
            torch.cuda.manual_seed(seed=SEED)
    
    logger.info(f"Device : {device}")
    return device

def get_random_number():
    return random.random()