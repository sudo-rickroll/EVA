This folder contains the end to end steps followed to train the CIFAR10 Dataset.

The folder contains 7 files:

1. S7.ipynb           -> Main Notebook File
2. graphs.py          -> Python Module to plot graphs for the obtained accuracies and losses
3. misclassified.py   -> Python Module to plot the images of 25 misclassified predictions
4. model.py           -> Python Module that contains the model to train the dataset
5. regularizations.py -> Python Module that contains the different regularization functions
6. test.py            -> Python Module that contains the function for running the model on the validation dataset
7. train.py           -> Python Module that contains the function for running the model and training it on the train dataset
8. utils.py           -> Python Module that contains the class required for loading of dataset, applying transformations and creation of dataloader

>This model uses normal 3\*3 and 1\*1 Convolutions along with atrous/dilated convolution and depthwise separable convolution in convolution layers and maxpool for transition layer. 

>It uses Global Average Pooling towards the end, coupled with a fully connected layer to reach the required number of channels for the dataset.

>>Parameters Used : 330,538

>>Number of Epochs : 25

>>Highest Validation Accuracy : 82.15% (Epoch 7)
