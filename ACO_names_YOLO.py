import json
import numpy as np
import matplotlib.image as mpimg
from skimage.transform import resize

with open('retail-product-checkout-dataset/instances_train2019.json', 
          encoding='utf-8-sig') as json_file:
    json_data_train = json.load(json_file) #Cargar anotaciones de train
  
f = open('train.txt',"w+")    
for i_id in range(np.size(json_data_train['images'])):   
    f.write('data/custom/images/'+'c_'+str(json_data_train['images'][i_id]['file_name'])+'\n')

f.close() 