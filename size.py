import shutil

from PIL import Image
import os
def read_size(label_file_name,images_dir):
    for images_file_name in os.listdir(images_dir):
        if os.path.splitext(label_file_name)[0] == os.path.splitext(images_file_name)[0]:
             with Image.open(os.path.join(images_dir,images_file_name)) as img:
                 return img.size
    raise FileNotFoundError(f"未找到与标签文件 {label_file_name} 对应的图片")

def yolo_read(label_file_name,labels_dir):
    yolo_size_lsts =[]
    with open(os.path.join(labels_dir,label_file_name)) as yolo_file:
        yolo_lists = yolo_file.readlines()
        for yolo_line in yolo_lists:
            yolo_value = yolo_line.strip().split()
            yolo_width,yolo_height=yolo_value[3],yolo_value[4]
            yolo_size_lsts.append([yolo_width,yolo_height])
    return yolo_size_lsts


def box_size(width,height,yolo_width, yolo_height):
    area = float(yolo_width) * width * float(yolo_height) *height
    if area <64:
        return '极小目标'
    elif 64<= area <16**2:
        return '微小目标'
    elif 16**2<=area<32**2:
        return '小目标'
    elif 32**2<=area<128**2:
        return '中目标'
    elif 128**2<=area:
        return '大目标'


def move(a):
    output_min_dir = r'C:\Users\Administrator\PycharmProjects\label\output_min_dir'
    os.makedirs(output_min_dir, exist_ok=True)
    if a == '极小目标':
        shutil.move(os.path.join(labels_dir,label_file_name),os.path.join(output_min_dir,f'move_{label_file_name}'))
        shutil.move(os.path.join(images_dir, f'{os.path.splitext(label_file_name)[0]}.jpg'), os.path.join(output_min_dir, f'move_{os.path.splitext(label_file_name)[0]}.jpg'))



if __name__=='__main__':
    images_dir = r'C:\Users\Administrator\PycharmProjects\label\label_images'
    labels_dir = r'C:\Users\Administrator\PycharmProjects\label\yolo'
    output_dir = r'C:\Users\Administrator\PycharmProjects\label\box_size_dir'

    os.makedirs(output_dir, exist_ok=True)
    for label_file_name in os.listdir(labels_dir):
        if label_file_name == 'classes.txt':
            continue
        width,height = read_size(label_file_name,images_dir)
        yolo_size_lsts = yolo_read(label_file_name,labels_dir)
        for yolo_size_lst in yolo_size_lsts:
            yolo_width, yolo_height = yolo_size_lst
            a = box_size(width, height, yolo_width, yolo_height)
            with open(os.path.join(output_dir,f'{label_file_name}_box_size'),'w',encoding='utf-8') as f :
                f.write(f'{label_file_name},{a}')






