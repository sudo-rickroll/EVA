This folder contains the end to end steps followed to train the CIFAR10 Dataset using the RESNET18 Module. It contains Albumentation transforms and GradCam implementation for the same.

The folder contains 10 files:

1. S7.ipynb           -> Main Notebook File
2. graphs.py          -> Python Module to plot graphs for the obtained accuracies and losses
3. misclassified.py   -> Python Module to plot the images of 25 misclassified predictions
4. model.py           -> Python Module that contains the RESNET18 model to train the dataset
5. regularizations.py -> Python Module that contains the different regularization functions
6. test.py            -> Python Module that contains the function for running the model on the validation dataset
7. train.py           -> Python Module that contains the function for running the model and training it on the train dataset
8. utils.py           -> Python Module that contains the class required for loading of dataset, applying transformations and creation of dataloader
9. AlbumentationTransformations.py -> Python Module that contains the methodologies for data augmentation using Albumentations.
10. GradCam.py        -> Python module that contains the implementation of GradCam.


>>Parameters Used : 11,173,962

>>Number of Epochs : 25

>>Highest Validation Accuracy : 87.97% (Epoch 24)
