import numpy as np
import cv2

def blur_add_img(image_path,kernel,lamb):
    img = cv2.imread(image_path)
    gao_si_img = cv2.GaussianBlur(img, (kernel, kernel), 1)
    new_img = cv2.addweighted(gao_si_img,lamb,img,1-lamb,1)
    return new_img