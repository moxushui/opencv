import numpy as np
import cv2

def sharpen(image_path,alph,beta,lamb):
    img = cv2.imread(image_path)
    canny_img = cv2.cannyImg = cv2.Canny(img,alph, beta)
    new_img = cv2.addweighted(canny_img,lamb,img,1-lamb,1)
    return new_img