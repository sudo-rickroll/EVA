This folder contains the steps followed during image annotation and data points collected after the same.

50 images were collected for classes with Masks, Hardhat, Vests and Boots and they were annotated with the VGG annotator present here - https://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html

The Bounding Boxes were drawn for the images and the JSON was generated for these annotations, which is included as the Annotations.json file. The metrics that were collected from the annotations have been described in the *Description of Annotations.txt* file.

The width of the bounding box, height of the bounding box, x-centroid of the bounding box and y-centroid of the bounding box were fetched from the JSON and were normalised using the height and width of the image. Then, the optimal number of clusters for the anchor box were found using the K-Means clustering technique. All these are included in the K-Means Clustering.ipynb file.
