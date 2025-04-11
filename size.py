from PIL import Image
import os
def read_size(label_file_name,images_dir):
    for images_file_name in os.listdir(images_dir):
        if os.path.splitext(label_file_name)[0] == os.path.splitext(images_file_name)[0]:
             with Image.open(os.path.join(images_dir,images_file_name)) as img:
                 width,height=img.size
                 return width,height

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




if __name__=='__main__':
    images_dir = r'D:\python\PythonProject\output_dir\images'
    labels_dir = r'D:\python\PythonProject\output_dir\labels'
    output_dir = r'D:\python\PythonProject\box_size_dir'

    os.makedirs(output_dir, exist_ok=True)
    for label_file_name in os.listdir(labels_dir):
        width,height =read_size(label_file_name,images_dir)
        yolo_size_lsts = yolo_read(label_file_name,labels_dir)
        for yolo_size_lst in yolo_size_lsts:
            yolo_width, yolo_height = yolo_size_lst
            os.makedirs('box_size_dir',exist_ok=True)
            with open(os.path.join(output_dir,f'{label_file_name}_box_size'),'w',encoding='utf-8') as f :
                f.write(label_file_name,box_size(width, height, yolo_width, yolo_height))






