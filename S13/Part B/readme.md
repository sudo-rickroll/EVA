This folder contains the training process of Images containing the classes "Mask", "Vest", "Hardhat" and/or "Boots" using the YOLO V3 using OpenCV by running the "train.py" file in the following repository -
https://github.com/theschoolofai/YoloV3

Sample Image of the Train Dataset:

![2ac971265e](https://user-images.githubusercontent.com/65642947/111881709-cd48b400-89d7-11eb-9bee-52b9ddff518b.jpg)


Status of Training:

![Train](https://user-images.githubusercontent.com/65642947/111882055-6af0b300-89d9-11eb-83c2-5798e479a0c4.JPG)


Further, a video from YouTube containing all 4 classes mentioned above is used to extract the frames (using FFMPEG) and the model is tested on the extracted frames by running the "detect.py" file from the same GitHub Repository mentioned above. The annotated frames are then converted to a video (using FFMPEG again).

Sample Image from the Test Output:

![Test](https://user-images.githubusercontent.com/65642947/111882131-d63a8500-89d9-11eb-935c-6eca69b6c2aa.JPG)


Link to the YouTube Video generated from the annotated output images :

[![](http://img.youtube.com/vi/VHYpHynVeSs/0.jpg)](http://www.youtube.com/watch?v=VHYpHynVeSs "YOLO V3 Object Detection")

