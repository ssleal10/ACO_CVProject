# ACO_ComputerVisionProject
Repository for the computer vision project
## To dowload the dataset:
1. Install kaggle API and API credentials.
2. Run "kaggle datasets download -d diyer22/retail-product-checkout-dataset"

## To train a model using the YOLO detector (done by: https://github.com/eriklindernoren/PyTorch-YOLOv3):
1. mkdir images 
2. Run "python3 ACO_save_crp_train.py"
3. Place the images folder obtained to PyTorch-YOLOv3/data/custom/images
4. mkdir labels
5. Run "python3 ACO_crp_YOLO.py"
6. Place the labels folder obtained to PyTorch-YOLOv3/data/custom/labels}
7. Run "--model_def config/yolov3-custom.cfg --data_config config/custom.data --epochs 7"
### To detect using the trained YOLO model.
1. Run "python3 detect.py --image_folder ../retail-product-checkout-dataset/val2019/ --model_def config/yolov3-custom.cfg --weights_path savedModel.pth --class_path data/custom/classes.names --conf_thres desiredConfidenceThreshold"
2. See results in output directory.

## Scripts description:
1. ACO_crp_YOLO.py - generates labels for training the YOLO detector.
2. ACO_for_syndata.py - generates image samples for syndata image generation.
3. ACO_names_YOLO.py	- generates necessary .txt for training the YOLO detector.
4. ACO_resize_val.py	- resizes validation set, not used in final results but used to test computation time and memory used.
5. ACO_save_crp_train.py	- generates image samples for trainining the YOLO detector.
6. ACO_savesub_crp_train.py - generates image samples in subfolders for syndata image generation.





