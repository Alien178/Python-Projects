import cv2
from sklearn.datasets import fetch_openml
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os, ssl, time

X, y = fetch_openml("mnist_784", version = 1, return_X_y = True)

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state = 9, test_size = 7500, train_size = 2500)

x_train_scaled = x_train / 255
x_test_scaled = x_test / 255

clf = LogisticRegression(solver = "saga", multi_class = "multinomial")
clf.fit(x_train_scaled, y_train)

def get_prediction(image):
    image_pil = Image.open(image)

    image_bw = image_pil.convert("L")

    image_bw_resize = image_bw.resize((28, 28), Image.ANTIALIAS)
    
    pixel_filter = 20

    min_pixel = np.percentile(image_bw_resize, pixel_filter)

    image_bw_resize_inverted_scaled = np.clip(image_bw_resize - min_pixel, 0, 255)

    max_pixel = np.max(image_bw_resize)

    image_bw_resize_inverted_scaled = np.asarray(image_bw_resize_inverted_scaled) / max_pixel

    test_sample = np.array(image_bw_resize_inverted_scaled).reshape(1, 784)

    test_predict = clf.predict(test_sample)

    return(test_predict[0])