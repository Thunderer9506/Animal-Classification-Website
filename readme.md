# 🐾 Animal Classification with YOLOv8 & Streamlit

A simple yet powerful web application built with Streamlit to classify animal images using a custom-trained YOLOv8 model. Upload an image and see the model predict which animal it is!

***

### ✨ Live Demo

> [**Animal Classification Website**](https://thunderer9506-animal-classification-website-home-ao1kf2.streamlit.app/)

***

### 📸 Screenshot

![App Screenshot](Screenshot/Home%20Page.png)

***

### 🚀 Features

* **Easy Image Upload**: Upload JPG images of animals through a simple drag-and-drop interface.
* **Instant Classification**: Get the predicted animal name with a single click.
* **Model Performance Insights**: View the model's training results and confusion matrix directly on the page.
* **Clean & Interactive UI**: A user-friendly and responsive interface powered by Streamlit.

***

### 🧠 Model Details

This project uses a **YOLOv8** classification model trained on a dataset of 15 different animal categories.

* **Architecture**: YOLOv8
* **Training Epochs**: 20
* **Input Image Size**: 64x64
* **Top-1 Accuracy**: ~98%

***

### 🐘 Supported Animals

The model can classify the following 15 animals:

| | | | | |
| :---: | :---: | :---: | :---: | :---: |
| Bear 🐻 | Bird 🐦 | Cat 🐱 | Cow 🐮 | Deer 🦌 |
| Dog 🐶 | Dolphin 🐬 | Elephant 🐘 | Giraffe 🦒 | Horse 🐴 |
| Kangaroo | Lion 🦁 | Panda 🐼 | Tiger 🐯 | Zebra 🦓 |

***

### 🛠️ Technologies Used

* **Frontend**: Streamlit
* **Model Framework**: Ultralytics YOLOv8, PyTorch
* **Image Processing**: Pillow (PIL)
* **Language**: Python

***

<p align="center">
  Created with ❤️ by Shaurya Srivastava
</p>