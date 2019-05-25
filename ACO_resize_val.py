#Codigo para visualizacion de las imagenes y anotaciones en TRAIN

import json
import numpy as np
import matplotlib.image as mpimg
from skimage.transform import resize
import os

os.mkdir('val2019resized')


#para leer una imagen y hacerle resize (downsampling)
def read_resize(filename):
    image = mpimg.imread(filename)

    imageOut = resize(image, (int(image.shape[0] / 4), int(image.shape[1] / 4)),
                       anti_aliasing=True)
    return imageOut


with open('retail-product-checkout-dataset/instances_val2019.json', 
          encoding='utf-8-sig') as json_file:
    json_data_val = json.load(json_file) #Cargar anotaciones de val


def save_crp_val(json_data_val,i_id):  
    str1='retail-product-checkout-dataset/val2019/'
    str2=json_data_val['images'][i_id]['file_name']
        
    filename = str1+str2
        
    image_out = read_resize(filename)
       
    mpimg.imsave('val2019resized'+'/'+'c_'+str2,image_out)
    return image_out


for i_id in range(np.size(json_data_val['annotations'])):
    image_bbox = save_crp_val(json_data_val,i_id)