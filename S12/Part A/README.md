This folder contains the end to end steps followed to train the tiny-imagenet Dataset using the RESNET18 Module. 

The folder contains 12 files:

1. S12.ipynb           -> Main Notebook File
2. graphs.py          -> Python Module to plot graphs for the obtained accuracies and losses
3. misclassified.py   -> Python Module to plot the images of 25 misclassified predictions
4. regularizations.py -> Python Module that contains the different regularization functions
5. test.py            -> Python Module that contains the function for running the model on the validation dataset
6. train.py           -> Python Module that contains the function for running the model and training it on the train dataset
7. utils.py           -> Python Module that contains the class required for loading of dataset, applying transformations and creation of dataloader
8. AlbumentationTransformations.py -> Python Module that contains the methodologies for data augmentation using Albumentations.
9. GradCam.py        -> Python module that contains the implementation of GradCam.
10. LR_Finder.py, Range_Test.py -> Python Modules that contain the code to find the optimal LR for use with Cyclic LR Scheduler
11. Data_Preparation.py -> Python Module that contains the code for preparing the tiny-imagenet datafor training.


>>Parameters Used : 11,689,512

>>Number of Epochs : 50

>>Highest Validation Accuracy : 35.10% (Epoch 50)
