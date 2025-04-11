import random
import numpy as np
import cv2

def random_zeros(image_path,nums,size:int):
    img = cv2.imread(image_path)
    h,w = img.shape[:2]
    for _ in range(nums):
        x = np.random.randint(size,w-size)
        y = np.random.randint(size,h-size)
        img[x:x+size,y:y+size]=0
    return img