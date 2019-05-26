# ACO_ComputerVisionProject
Repository for the computer vision project


Methodology implemented for the YOLO detector:

Having the crop images at each view of each instance of the products, a YOLO detector was trained without using a domain translation method. The parameters used were; learning rate: 0.001 Decay: 0.0005 batch: 5 momentum: 0.9. No angle variation was taken in to account into the detector at first. Then, after training for 7 epochs the model was used to detect on the validation set. After detecting on the validation dataset the results were visualized first using a confidence threshold of 0.7. After, detections were made using the same trained model with a confidence threshold of 0.5. 

Then a new model was trained using the same parameters that the last one but trained after 10 epochs. This model was used to detect and the resuslts were visulized using a confidende threshold of 0.7.

Finally, a model was trained using the same parameters that the last ones, but this time angle variations, maximum 90 degrees, were considered. Then the model was used to detect on the validation dataset for different values of confidence threshold.


Considering the several limitations that the model tends to present because of the lack of a domain translation method. syndata-generation method proposed by [cite] was adopted. For that purpose, segmentation mask were required ...
