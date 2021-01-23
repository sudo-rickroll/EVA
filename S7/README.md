This file contains the end to end steps followed to train the CIFAR10 Dataset.

>This model uses normal 3\*3 and 1\*1 Convolutions along with atrous/dilated convolution and depthwise separable convolution in convolution layers and maxpool for transition layer. 

>It uses Global Average Pooling towards the end, coupled with a fully connected layer to reach the required number of channels for the dataset.

>>Parameters Used : 330,538

>>Number of Epochs : 25

>>Highest Validation Accuracy : 82.15% (Epoch 7)
