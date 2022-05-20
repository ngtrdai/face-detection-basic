# @author: Nguyen Trong Dai
# @date: 20/05/2022
# @file: createDataset.py

import numpy as np
import cv2 as cv

camera = cv.VideoCapture(0)

count = 0
countFrame = 0
label = "not_ngtrdai"
while count < 50:
    countFrame += 1
    ret, frame = camera.read()
    if not ret:
        continue

    frame = cv.resize(frame, dsize=None,fx=0.3,fy=0.3)
    cv.imshow('Camera', frame)
    if countFrame >= 30:
        countFrame = 0
        cv.imwrite('datasets/' + str(label) + "_" + str(count) + ".png",frame)
        count += 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
camera.release()
cv.destroyAllWindows()