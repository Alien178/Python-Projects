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

#Setting an HTTPS Context to fetch data from OpenML 
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

X, y = fetch_openml("mnist_784", version = 1, return_X_y = True)
print(pd.Series(y).value_counts())

classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nClasses = len(classes)

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state = 9, test_size = 7500, train_size = 2500)

x_train_scaled = x_train / 255
x_test_scaled = x_test / 255

clf = LogisticRegression(solver = "saga", multi_class = "multinomial")
clf.fit(x_train_scaled, y_train)

y_predict = clf.predict(x_test_scaled)
accuracy = accuracy_score(y_test, y_predict)

print(accuracy)

cap = cv2.VideoCapture(0)

while True:
    try:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        height, width = gray.shape
        upper_left = (int(width / 2 - 56), int(height / 2 - 56))
        bottom_right = (int(width / 2 + 56), int(height / 2 + 56))
        
        cv2.rectangle(gray, upper_left, bottom_right, (0, 255, 0), 2)

        roi = gray[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]

        image_pil = Image.fromarray(roi)

        image_bw = image_pil.convert("L")

        image_bw_resize = image_bw.resize((28, 28), Image.ANTIALIAS)

        image_bw_resize_inverted = PIL.ImageOps.invert(image_bw_resize)
        
        pixel_filter = 20

        min_pixel = np.percentile(image_bw_resize_inverted, pixel_filter)

        image_bw_resize_inverted_scaled = np.clip(image_bw_resize_inverted - min_pixel, 0, 255)

        max_pixel = np.max(image_bw_resize_inverted)

        image_bw_resize_inverted_scaled = np.asarray(image_bw_resize_inverted_scaled) / max_pixel

        test_sample = np.array(image_bw_resize_inverted_scaled).reshape(1, 784)

        test_predict = clf.predict(test_sample)

        print("Predicted Class:", test_predict)

        cv2.imshow("frame", gray)

        if cv2.waitKey(1) and 0XFF == ord("q"):
            break
    
    except Exception as e:
        pass

cap.release()
cv2.destroyAllWindows()