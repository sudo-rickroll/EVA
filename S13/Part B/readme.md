# YOLO V3 Object Detection

This folder contains the training process of images containing the classes "Mask", "Vest", "Hardhat" and/or "Boots" using the YOLO V3 using OpenCV by running the "train.py" file in the Yolo V3 folder. The Yolo V3 folder contains all the assets related to the training and testing of this architecture.

## Sample Image from the Train Dataset:

![2ac971265e](https://user-images.githubusercontent.com/65642947/111881709-cd48b400-89d7-11eb-9bee-52b9ddff518b.jpg)



## Status of Training:

![Train](https://user-images.githubusercontent.com/65642947/111882055-6af0b300-89d9-11eb-83c2-5798e479a0c4.JPG)


Further, a video from YouTube containing all 4 classes mentioned above is used to extract the frames (using FFMPEG) and the model is tested on the extracted frames by running the "detect.py" file from the same GitHub Repository mentioned above. The annotated frames are then converted to a video (using FFMPEG again).

## Sample Image from the Test Output:

![image-280](https://user-images.githubusercontent.com/65642947/111882333-0b93a280-89db-11eb-9100-b34f2d752ba1.jpg)



## Link to the YouTube Video generated from the annotated output images (Click on the image below to be redirected to the YouTube video):

[![](http://img.youtube.com/vi/VHYpHynVeSs/0.jpg)](http://www.youtube.com/watch?v=VHYpHynVeSs "YOLO V3 Object Detection")

