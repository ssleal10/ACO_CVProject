# RPC_ComputerVisionProject

Repository for the computer vision project / Retail Product Checkout Dataset

## To run the DEMO & TEST (Detections & Precision/Recall) using the trained YOLO model.

1. cd PyTorch-YOLOv3
2. Run "python3 demo.py"
3. See more results in output directory.

To evaluate results (get precision and recall) obtained in demo:

1. Run "python3 test.py"

The script PR_curve.py depicts the precision-recall curve presentend in the paper obtained using several confidence thresholds for a specific model. In there precision and recall are the ones obtained for non domain translated model. 

### To download the dataset

1. Install kaggle API and API credentials. ( Read: https://github.com/Kaggle/kaggle-api )
2. Run "kaggle datasets download -d diyer22/retail-product-checkout-dataset"

### To train a model using the YOLO detector ( done by: https://github.com/eriklindernoren/PyTorch-YOLOv3 )

1. mkdir images 
2. Run "python3 ACO_save_crp_train.py"
3. Place the images folder obtained to PyTorch-YOLOv3/data/custom/images
4. mkdir labels
5. Run "python3 ACO_crp_YOLO.py"
6. Place the labels folder obtained to PyTorch-YOLOv3/data/custom/labels
7. Run "python3 train.py --model_def config/yolov3-custom.cfg --data_config config/custom.data --epochs 7"

### To generate multiple product images ( Domain-Translation, done by: https://github.com/debidatta/syndata-generation )

1. Install required libraries. ( Read: https://github.com/debidatta/syndata-generation )
2. Get poisson blending library. ( Read: https://github.com/yskmt/pb )
3. Modify defaults.py as desired.
4. Run "python2 dataset_generator.py *path_to_ACO_for_syndata.py_output* *outputDesiredDirectory*
#### syndata-generation Python3 version available at: ( https://github.com/yueweiyang/syndata-generation *has issues* )

### Scripts description
1. ACO_crp_YOLO.py - generates labels for training the YOLO detector.
2. ACO_for_syndata.py - generates image samples for syndata image generation.
3. ACO_names_YOLO.py	- generates necessary .txt for training the YOLO detector.
4. ACO_resize_val.py	- resizes validation set, not used in final results but used to test computation time and memory used.
5. ACO_save_crp_train.py	- generates image samples for trainining the YOLO detector.
6. ACO_savesub_crp_train.py - generates image samples in subfolders for syndata image generation.
7. PyTorch-YOLOv3/PR-curve.py - depicts the precision recall curve presented on the paper.
8. PyTorch-YOLOv3/demo.py - performs detection on a sample image and generates results.
9. PyTorch-YOLOv3/test.py - if ran before demo.py: evaluates (gets precision and recall) the results obtained in the validation dataset. 
                          - if ran after demo.py: evaluates (gets precision and recall) the results obtained in the demo images.




