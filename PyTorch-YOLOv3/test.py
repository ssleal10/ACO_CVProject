import matplotlib.image as mpimg
from skimage.transform import resize
import os
import urllib.request
import json
# Carga el .txt (Results.txt)de resultados generados por demo.py y detect.py 
# y calcula precisión y cobertura.
print('Downloading data...')
url = 'https://www.dropbox.com/s/anvgpasg9t022cl/instances_val2019.json?dl=1'  
urllib.request.urlretrieve(url,'instances_val2019.json')
print('Done!')

with open('instances_val2019.json', 
          encoding='utf-8-sig') as json_file:
    json_data_val = json.load(json_file) #Cargar anotaciones de val
    
    
file = open("Results.txt","r")
line = file.readline()
TP = 0
FP = 0
FN = 0
while line != "":
    item = line.split(";")
    name = item[0]
    name = name.replace('val2019p/','')
    predictions = item[1].split(",")
    if ": \n" in predictions: predictions.remove(": \n")    
    outdict= [item for item in json_data_val['images'][:] if item["file_name"] == name]
    id_img=outdict[0]['id']
    annotations= [item for item in json_data_val['annotations'][:] if item["image_id"] == id_img]
    anot = []
    for i in range(len(annotations)):
        it = str(annotations[i]['category_id'])
        anot.append(it)
        #print(anot)
    coincidences = [i for i in predictions if i in anot]
    if coincidences != []:
        TP = TP + len(coincidences)
        FP = FP +(len(predictions)-len(coincidences))
        FN = FN + (len(annotations)-len(coincidences))
    elif coincidences == []:
        FP = FP + len(predictions)
        FN + (len(annotations))
    line = file.readline()
    
    #prueba = [1 , 2 ,3]
    #prueba2 = [2 , 4 ,5]
file.close()

print('# True Positives:',TP)
print('# False Positives:',FP)
print('# False Negatives:',FN)
if (TP+FP) == 0:
    Precision = 0
else:
    Precision = TP / (TP+FP)
if (TP+FN) == 0:
    Recall = 0
else:
    Recall = TP /(TP+FN)
    
print('Precision:',Precision)
print('Recall:',Recall)
