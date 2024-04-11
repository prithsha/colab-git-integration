import albumentations as A
from albumentations.pytorch import ToTensorV2


def compose_custom_transforms(transforms_collection : list):
        return A.Compose(transforms_collection)


def create_basic_transforms_collection(mean : tuple= (0.4914, 0.4822, 0.4465), std :tuple= (0.2470, 0.2435, 0.2616)):
    transforms_collection  = [ A.Normalize(mean=mean, std=std),
                               ToTensorV2()]
    
    return transforms_collection

def create_shift_scale_rotate_transform(shift_limit = 0.1, scale_limit = 0.1, rotate_limit = 10, p = 0.25):
    return A.ShiftScaleRotate(shift_limit=shift_limit, scale_limit=scale_limit, rotate_limit=rotate_limit, p=p)



def create_coarse_drop_out_transformation(hole_size : tuple =(8,8), fill_value = [0,0,0], p=0.5):     
     return A.CoarseDropout(max_holes=1, min_holes=1, 
                            max_height=hole_size[0], max_width=hole_size[1],
                            min_height=hole_size[0], min_width=hole_size[1],
                            p=p, fill_value=fill_value)


def create_random_resize_crop_transformation(zoom_image_size : tuple= (40,40), random_crop_size: tuple=(32,32), final_image_size: tuple=(32,32)):
    return [A.PadIfNeeded(min_height=zoom_image_size[0], min_width=zoom_image_size[1], always_apply=True),     
            A.RandomCrop(height=random_crop_size[0], width=random_crop_size[1], always_apply=True),
            A.Resize(height=final_image_size[0], width=final_image_size[1], always_apply=True)]


def create_flip_transformation(is_horizontal = True, is_random = False, p= 0.25):
    if(is_random):
        return A.Flip(p=p)
    if(is_horizontal):
        return A.HorizontalFlip(p=p)
    else:
         return A.VerticalFlip(p=p)
