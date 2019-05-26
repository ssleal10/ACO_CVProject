#Codigo para visualizacion de las imagenes y anotaciones en TRAIN

import json
import numpy as np
import matplotlib.image as mpimg
from skimage.transform import resize
import os
from PIL import Image


os.mkdir('imagesn')

#para leer una imagen 
def readPBM(filename):
    image = Image.open(filename)
    return image

#para leer una imagen 
def read(filename):
    image = mpimg.imread(filename)
    return image


##save img as PBM
def toPBM(filename):
    im = Image.open(filename)
    im.save('myfile.pbm')


#para leer una imagen y cortar con bbox extendido
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
    str1='run-1xx-sal-c/' #path de la carpeta de las mascaras
    str2=json_data_train['images'][i_id]['file_name']
    str3=json_data_train['annotations'][i_id]['category_id']
        
    filename = str1+'c_'+str2[0:-4]+'_sal_fuse.png'

    image_bbox = read(filename)
    
    image_out = resize(image_bbox, (np.int(image_bbox.shape[0] / 4), np.int(image_bbox.shape[1] / 4)),
                       anti_aliasing=True)
    
    if not os.path.exists('imagesn'+'/'+str(str3)):
        os.makedirs('imagesn'+'/'+str(str3))

    temp_filename = 'temp.png' #archivo de imagen temporal, para abrirla con PIL
    mpimg.imsave(temp_filename,image_out)
    
    I = image_out

    I8 = (((I - I.min()) / (I.max() - I.min())) * 255.9).astype(np.uint8)

    img = Image.fromarray(I8)
    img.save('imagesn'+'/'+str(str3)+'/'+'c_'+str2[0:-4]+'_sal_fuse.png')
    
    image_out = readPBM(temp_filename)    
    image_out.save('imagesn'+'/'+str(str3)+'/'+'c_'+str2[0:-4]+'_sal_fuse.pbm')    
    
    
    return image_out, image_bbox




for i_id in range(np.size(json_data_train['annotations'])):
    image_out,image_bbox = save_crp_train(json_data_train,i_id)
    
    #if i_id==500:
    #    break