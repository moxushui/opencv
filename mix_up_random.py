import random
import numpy as np
import cv2
def mix_up_random(image_path):
    rnd_img = np.random.randn(*image_path.shape).astype(np.unit8)
    mix_up_img = cv2.addweighted(image_path,0.5,rnd_img,0.5,0)
    return mix_up_img