This folder consists of models written for MNIST in the following order:

1. Model using Batch Normalisation and L1 Regularisation only.
2. Model containing Batch Normalisation and L2 Regularisation only.
3. Model containing Batch Normalisation and both L1 and L2 Regularisation.
4. Model containing the recently introduced Ghost Batch Normalisation.
5. Model containing Ghost Batch Normalisation and both L1 and L2 Regularisation.

There are two images that shows the plot of Validation Accuracy and Validation loss. The third image represents a set of 25 misclassified images during the training of the 4th model mentioned above.

The highest accuracy was obtained using the 4th model mentioned above. The results can be further finetuned by tweaking the L1 and L2 Regularisation parameters. It was observed that for accuracy to be improved, these values needed to be kept as small as possible.

