from matplotlib import pyplot as plt
import math

import matplotlib.pyplot as plt
import numpy as np
# OpenCV のインポート
import cv2

cap = cv2.VideoCapture(0)

times = [0 for i in range(100)]
means = [0 for i in range(100)]

time = 0
mean = 0

# initialize matplotlib
plt.ion()
plt.figure()
li, = plt.plot(times, means)

plt.ylim(0,256)
plt.ylabel("brightness value")
plt.title("real time plot")

while True :

    time += 0.1

    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    #frame = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))
    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)          

    mean = frame.mean()

    times.append(time)
    times.pop(0)
    means.append(mean)
    means.pop(0)

    li.set_xdata(times)
    li.set_ydata(means)
    plt.xlim(min(times), max(times))
    plt.draw()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    plt.pause(0.01)

cap.release()
cv2.destroyAllWindows()