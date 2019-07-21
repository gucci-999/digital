import matplotlib.pyplot as plt
import time

# OpenCV のインポート
import cv2

# VideoCaptureのインスタンスを作成する
cap = cv2.VideoCapture(0)

xs = [0 for i in range(100)]
means = [0 for i in range(100)]

t1 = time.time()
x = 0
mean = 0

plt.ion()
plt.figure()
li, = plt.plot(xs, means)

plt.ylim(0,256)
plt.ylabel("brightness value")
plt.title("real time plot")

while True :

    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)          

    t2 = time.time()
    mean = frame.mean()
    x = t2-t1

    xs.append(x)
    xs.pop(0)
    means.append(mean)
    means.pop(0)

    li.set_xdata(xs)
    li.set_ydata(means)
    plt.xlim(min(xs), max(xs))
    plt.draw()

    # キー入力を1ms待って、k がqだったらBreakする
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()