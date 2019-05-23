#Codigo para visualizacion de las imagenes y anotaciones en TRAIN

import json
import numpy as np
import matplotlib.image as mpimg
from skimage.transform import resize
import os

os.mkdir('images')

#para leer una imagen 
def read(filename):
    image = mpimg.imread(filename)
    return image

#para leer una imagen y cortar en su posicion central
def read_crop(filename,x_point,y_point,dist_aum_center):
    image = mpimg.imread(filename)
    image = image[(y_point-dist_aum_center):(y_point+dist_aum_center),
                  (x_point-dist_aum_center):(x_point+dist_aum_center)]
    return image

#para leer una imagen y cortar con bbox
def read_crop_bbox(filename,x_img, y_img,width_img,height_img):
    image = mpimg.imread(filename)
    image = image[(y_img):(y_img+height_img),
                  (x_img):(x_img+width_img)]
    return image

#para leer una imagen y cortar con bbox
def read_crop_bbox_ext(filename,x_img,y_img,width_img,height_img,ext_w,ext_h):
    image = mpimg.imread(filename)
    image = image[(y_img-ext_h):(y_img+height_img+ext_h),(x_img-ext_w):(x_img+width_img+ext_w)]
    return image


#para leer una imagen, cortar en su posicion central y hacerle resize (downsampling)
def read_crop_resize(filename,x_point,y_point,dist_aum_center,factor_resize):
    image = mpimg.imread(filename)
    image = image[(y_point-dist_aum_center):(y_point+dist_aum_center),
                  (x_point-dist_aum_center):(x_point+dist_aum_center)]
    image = resize(image, (np.int(np.floor(image.shape[0] / factor_resize)), 
                           np.int(np.floor(image.shape[1] / factor_resize))),
                       anti_aliasing=True)
    return image

with open('retail-product-checkout-dataset/instances_train2019.json', 
          encoding='utf-8-sig') as json_file:
    json_data_train = json.load(json_file) #Cargar anotaciones de train

with open('retail-product-checkout-dataset/instances_val2019.json', 
          encoding='utf-8-sig') as json_file:
    json_data_val = json.load(json_file) #Cargar anotaciones de val


def save_crp_train(json_data_train,i_id):  
    str1='retail-product-checkout-dataset/train2019/'
    str2=json_data_train['images'][i_id]['file_name']
    str3=json_data_train['annotations'][i_id]['category_id']
        
    filename = str1+str2
    x_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][0])) #bbox x-coord
    y_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][1])) #bbox y-coord
    width_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][2])) #bbox width
    height_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][3])) #bbox height
    

    ext_w = int(np.floor(width_img/8))
    ext_h = int(np.floor(height_img/8))
    
    if y_img-ext_h<=0 and x_img-ext_w<=0:
        bbox_crp = (x_img,y_img,width_img,height_img)
    elif y_img-ext_h>0 and x_img-ext_w<=0:
        bbox_crp = (x_img,ext_h,width_img,height_img)
    elif y_img-ext_h<=0 and x_img-ext_w>0:
        bbox_crp = (ext_w,y_img,width_img,height_img)
    elif y_img-ext_h>0 and x_img-ext_w>0:
        bbox_crp = (ext_w,ext_h,width_img,height_img)
    
    if y_img-ext_h<=0:
        y_img=ext_h+1
    if x_img-ext_w<=0:
        x_img=ext_w+1
        
    image_bbox = read_crop_bbox_ext(filename,x_img,y_img,width_img,height_img,ext_w,ext_h)
    
    image_out = resize(image_bbox, (int(image_bbox.shape[0] / 4), int(image_bbox.shape[1] / 4)),
                       anti_aliasing=True)
    

    if not os.path.exists('images'+'/'+str(str3)):
        os.makedirs('images'+'/'+str(str3))
    
    mpimg.imsave('images'+'/'+str(str3)+'/'+'c_'+str2,image_out)
    return image_out


for i_id in range(np.size(json_data_train['annotations'])):
    image_bbox = save_crp_train(json_data_train,i_id)