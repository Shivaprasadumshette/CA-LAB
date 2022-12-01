import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
Chess= cv2.imread("Chess.png")
Chess= cv2.resize(Chess, (400, 400))
s = Chess.shape
print(s)
cv2.imshow('Original', Chess)
ChessGray = cv2.cvtColor(Chess, cv2.COLOR_BGR2GRAY)
ChessGray = cv2.convertScaleAbs(ChessGray, alpha=1.10, beta=-20)
cv2.imshow('Binary', ChessGray)


def Hist(image):
    H = np.zeros(shape=(256, 1))
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            k = image[i, j]
            H[k, 0] = H[k, 0] + 1
    return H


histg = Hist(ChessGray)
plt.plot(histg)
x = histg.reshape(1, 256)
y = np.array([])
y = np.append(y, x[0, 0])
for i in range(255):
    k = x[0, i+1]+y[i]
    y = np.append(y, k)
y = np.round((y/(s[0]*s[1]))*(256-1))
for i in range(s[0]):
    for j in range(s[1]):
        k = ChessGray[i, j]
        ChessGray[i, j] = y[k]
equal = Hist(ChessGray)
cv2.imshow("myequalize", ChessGray)
plt.plot(equal)
plt.show()
cv2.waitKey(0)
