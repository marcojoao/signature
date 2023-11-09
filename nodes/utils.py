import torch
import numpy as np

def image_array_to_torch(image_np):
    img = image_np.get_float_value().transpose((2, 0, 1))
    return torch.tensor(img, dtype=torch.float32)