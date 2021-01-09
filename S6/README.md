# EVA

***************NOTEBOOK 1*****************

Target:

Prepare the skeleton structure
Apply transformations on dataset
Prepare convolution and transition blocks instead of single layers.
Test the model on single image and batch of images
Record the basic flow

Results:

Parameters: 43994
Best Training Accuracy: 98.135%
Best Test Accuracy: 98.08%

Analysis:

Too many parameters than what is required
Model is over-fitting and accuracy is not upto the mark


***************NOTEBOOK 2******************

Target:

Model needs to be slightly changed for the following reasons:

Reduce the number of parameters to less than 20000.
Hit an accuracy of 99.4% pretty consistently with the use of batch normalisation and dropout.

Results:

Parameters: 16030
Best Training Accuracy: 98.286%
Best Test Accuracy: 99.5%

Analysis:

Model is underfitting.
Parameters need to be further reduced and this needs to be compensated with other operations, which will be done in the upcoming models.


*********************NOTEBOOK 3***************************

Target:

Add data augmentation to slightly increase the accuracy.
Observe change in accuracy compared to previous model's max accuracy.

Results:

Parameters: 16030
Best Training Accuracy: 99.16%
Best Test Accuracy: 99.6%

Analysis:

Model is underfitting.
Accuracy seems to be improved by applying data augmentation but too many augmentations seem to impact the performance.


******************NOTEBOOK 4***********************

Target:

Model needs to be slightly changed for the following reasons:

Reduce the number of parameters to less than 10000. Compensate this by adding a convolution layer with padding and tune the learning rate and reduce batch size
Hit an accuracy of 99.4% consistently.

Results:

Parameters: 8790
Best Training Accuracy: 98.038%
Best Test Accuracy: 99.48%

Analysis:

Model is underfitting.
Learning rate can further be tuned to increase accuracy.
