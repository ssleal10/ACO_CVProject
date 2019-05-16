#Codigo para visualizacion de las imagenes y anotaciones en TRAIN

import json
import numpy as np
import matplotlib.image as mpimg
from skimage.transform import resize

#para leer una imagen y cortar con bbox EXTENDIDOS
def read_crop_bbox_ext(filename,x_img,y_img,width_img,height_img,ext_w,ext_h):
    image = mpimg.imread(filename)
    image = image[(y_img-ext_h):(y_img+height_img+ext_h),
                  (x_img-ext_w):(x_img+width_img+ext_w)]
    #size_image = (height_img+2*ext_h,height_img+2*ext_h)
    return image


with open('retail-product-checkout-dataset/instances_train2019.json', 
          encoding='utf-8-sig') as json_file:
    json_data_train = json.load(json_file) #Cargar anotaciones de train


def save_crp_train(json_data_train,i_id):  
    str1='retail-product-checkout-dataset/train2019/'
    str2=json_data_train['images'][i_id]['file_name']
        
    filename = str1+str2
    x_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][0])) #bbox x-coord
    y_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][1])) #bbox y-coord
    width_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][2])) #bbox width
    height_img = np.int(np.floor(json_data_train['annotations'][i_id]['bbox'][3])) #bbox height
    category_id = json_data_train['annotations'][i_id]['category_id'] #id de la categoria a la que pertenece


    ext_w = int(np.floor(width_img/8))
    ext_h = int(np.floor(height_img/8))
    if y_img-ext_h<=0:
        y_img=ext_h+1
    if x_img-ext_w<=0:
        x_img=ext_w+1
        
    image_bbox = read_crop_bbox_ext(filename,x_img,y_img,width_img,height_img,ext_w,ext_h)
    image_shape = image_bbox.shape
    img_y = image_shape[0]
    img_x = image_shape[1]
    bbox_crp = (filename,ext_w, ext_h,width_img,height_img)
    
    #mpimg.imsave('images/c_'+str2,image_bbox)
    bbox_crp = ('c_'+str2,ext_w, ext_h,width_img,height_img,category_id)
    
    x_center = ext_w + int(np.floor(width_img/2))
    y_center = ext_h + int(np.floor(height_img/2))
    bbox_crp_center = ('c_'+str2,x_center/img_x,y_center/img_y,width_img/img_x,height_img/img_y,category_id)
    
    return image_bbox, bbox_crp, bbox_crp_center


for i_id in range(np.size(json_data_train['annotations'])):
    image_bbox,bbox_crp,bbox_crp_center = save_crp_train(json_data_train,i_id)
    
    f = open('labels/'+bbox_crp_center[0][0:-4]+'.txt',"w+")
    f.write(str(bbox_crp_center[5])+' '+str(bbox_crp_center[1])+' '+str(bbox_crp_center[2])+' '+str(bbox_crp_center[3])+' '+str(bbox_crp_center[4])+'\n')
    f.close()


