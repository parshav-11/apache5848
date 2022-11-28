import numpy as np
import os
import cv2
import time
import shutil
from PIL import Image
import matplotlib.pyplot as plt
import keras_ocr

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

image_frames = r'E:\PyPi Project\image_frames'
def files():
    try:
        if not os.path.exists(image_frames):
            os.makedirs(image_frames)
    except OSError:
        pass
    #specify the source of video file
    src_vid = cv2.VideoCapture(0)
    return src_vid

def process(src_vid):
    #Use an index to integer-name the files
    while src_vid.isOpened():
        ret, frame = src_vid.read()
        frame = frame[200:920,140:450]
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        _, threshold = cv2.threshold(gray_frame, 115, 255, cv2.THRESH_BINARY)
        time.sleep(1)
        cv2.imshow('frame', threshold)
        if not ret:
            break
        
        index = 0
        #name each frame and save an image
        name = "./image_frames/frame" +str(index)+ ".png"
        #save every 100th frame
        if index % 1 == 0:
            cv2.imwrite(name, threshold)
            index += 1
#         for i in os.listdir(image_frames):
#             my_example = Image.open(r'C:\Users\madhu\image_frames\frame0.png')
#             text = pytesseract.image_to_string(my_example)
#             print(text)
        #shutil.rmtree(image_frames)
        images = [keras_ocr.tools.read(threshold) for threshold in [r'E:\PyPi Project\image_frames\frame0.png']]
        prediction_groups = pipeline.recognize(images)
        # Plot the predictions
        fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
        for ax, image, predictions in zip(axs, images, prediction_groups):
            keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    src_vid.release()
    cv2.destroyAllWindows()
    

#main driver
if __name__ == '__main__':
#     files()
    vid = files()
    process(vid)
