import numpy as np
import cv2
import random

def blur_img(image_path):
    img = cv2.imread(image_path)
    rnd_num = random.randint(1, 3)
    rnd_ksize = random.choice([5, 9, 13, 15])
    if rnd_num == 1:
        filter_img = cv2.blur(img, (rnd_ksize, rnd_ksize))
        return filter_img
    elif rnd_num == 2:
        filter_img = cv2.GaussianBlur(img, (rnd_ksize, rnd_ksize), 1)
        return filter_img
    elif rnd_num == 3:
        filter_img = cv2.medianBlur(img, rnd_ksize, 1)
        return filter_img
