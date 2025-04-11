import random
import numpy as np
import cv2
import os




def box_size(image_path,label_dir):
    image = os.path.basename(image_path)
    image_name = os.path.splitext(image)[0]
    box_size_lst = []
    for label_file in os.listdir(label_dir):
        if image_name == os.path.splitext(label_file)[0]:
            with open(os.path.join(label_dir,label_file),'r') as f :
                label_lines = f.readlines()
                for label_infor in label_lines:
                    x,y,w,h = label_infor.strip().split()[1:]
                    box_size_lst.append([w,h])
                return box_size_lst


def box_random_zeros(image_path,label_dir,nums,size):
    img = cv2.imread(image_path)
    img_h ,img_w = img.shape[:2]
    box_size_lsts=box_size(image_path,label_dir)
    for box_size_lst in box_size_lsts:
        x,y,w,h =float(box_size_lst)
        width = w*img_w
        height = h * img_h
        xmin = (x-w/2)*img_w
        ymin = (y-h/2)*img_h
        xmax = xmin + width
        ymax = ymin+ height
        for _ in range(nums):
            x = np.random.randint(xmin+size,  xmax- size)
            y = np.random.randint(ymin+size, ymax - size)
            img[x:x + size, y:y + size] = 0
        return img



