# Emotion recognition bot

------------
#### Table of Content :
1.[Introduction](#introduction)

2.[Dependencies](#dependencies)

3.[Dataset](#dataset)

4.[Basic Usage](#basic-usage)

5.[Algorithm](#algorithm)

6.[MTCNN](#mtcnn)

7.[CNN](#cnn)

------------


## Introduction

This project aims to classify the emotions on a person's face into one of three categories: happy, neutral, sad. Multitasking Cascade Convolution Network (MTCNN), Convolutional neural network (CNN) convolutional networks are used.
MTCNN is pre-trained, CNN is trained on the FER-2013 dataset, which was published at the International Conference on Machine Learning (ICML). This dataset consists of 35887 grayscale 48x48 face images with seven emotions - anger, disgust, fear, happiness, neutrality, sadness and surprise. From it, three of the desired ones are selected.

## Dependencies

* Python 3, [OpenCV](https://opencv.org/), [Tensorflow](https://www.tensorflow.org/)
* To install the required packages, run `pip install -r requirements.txt`.

# Dataset:

[Fer2013](https://www.kaggle.com/c/3364/download-all) dataset

-fer2013 emotion classification test accuracy: 66%

## Basic Usage

The repository is currently compatible with `tensorflow-2.0` and makes use of the Keras API using the `tensorflow.keras` library.

* First, clone the repository and enter the folder

```bash
git clone https://github.com/alexandrpon/Emotion-Recognition-Bot.git
cd Emotion-Recognition-Bot
```

* If you want to train CNN model: 

1. Take the pre-trained model from the [Google drive](https://drive.google.com/drive/folders/1JGY478oI5c1bsMrH5o5VNNawiVf0lQhe?usp=sharing)

2. Download [Fer2013](https://www.kaggle.com/c/3364/download-all) dataset

3. Change csv_path to your Fer path

4. Change model_name to your model path

5. Run train.ipynb


* If you want to view the predictions , you can download the pre-trained model from [Google drive](https://drive.google.com/drive/folders/1JGY478oI5c1bsMrH5o5VNNawiVf0lQhe?usp=sharing) and then download model to `"ML\Emotion_Recognition\model"`

* Create config file with your tg bot credits

* With a simple 3-layer CNN, the test accuracy reached 77.4% in 25 epochs.
  ![](https://github.com/alexandrpon/Emotion-Recognition-Bot/blob/master/images/graph.png)

## Algorithm
- First, MTCNN is used to detect faces in an image uploaded to the bot

- The region of image containing the face is resized to 48x48 and is passed as input to the CNN
![](https://github.com/alexandrpon/Emotion-Recognition-Bot/blob/master/images/rescale.png)
- The network outputs a list of scores for the three classes of emotions

- The emotion with maximum score is returned to user

## MTCNN
Stage 1: The Proposal Network (P-Net)
![](https://github.com/alexandrpon/Emotion-Recognition-Bot/blob/master/images/pnet.png)
This first stage is a fully convolutional network (FCN). The difference between a CNN and a FCN is that a fully convolutional network does not use a dense layer as part of the architechture. This Proposal Network is used to obtain candidate windows and their bounding box regression vectors.

Bounding box regression is a popular technique to predict the localization of boxes when the goal is detecting an object of some pre-defined class, in this case faces. After obtaining the bounding box vectors, some refinement is done to combine overlapping regions. The final output of this stage is all candidate windows after refinement to downsize the volume of candidates.

Stage 2: The Refine Network (R-Net)
![](https://github.com/alexandrpon/Emotion-Recognition-Bot/blob/master/images/rnet.png)
All candidates from the P-Net are fed into the Refine Network. Notice that this network is a CNN, not a FCN like the one before since there is a dense layer at the last stage of the network architecture. The R-Net further reduces the number of candidates, performs calibration with bounding box regression and employs non-maximum suppression (NMS) to merge overlapping candidates.

The R-Net outputs wether the input is a face or not, a 4 element vector which is the bounding box for the face, and a 10 element vector for facial landmark localization.

Stage 3: The Output Network (O-Net)
![](https://github.com/alexandrpon/Emotion-Recognition-Bot/blob/master/images/onet.png)
This stage is similar to the R-Net, but this Output Network aims to describe the face in more detail and output the five facial landmarks’ positions for eyes, nose and mouth.

## CNN
![](https://github.com/alexandrpon/Emotion-Recognition-Bot/blob/master/images/model_plot.png)
