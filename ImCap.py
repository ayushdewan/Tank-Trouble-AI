import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2, time
from PIL import Image
from colorlabeler import findTankCentroid
from linedetecttest import lineFind, raytrace
from keyboard import shoot, forward


def takeimage():
    global boom
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0,373,160,693,430)
    qimage1 = desktopPixmap.toImage()
    bytes =qimage1.bits().asstring(qimage1.byteCount())
    pilimg = Image.frombuffer("RGBA",(qimage1.width(),qimage1.height()),bytes,'raw', "RGBA", 0, 1)
    boom = np.array(pilimg)
    return boom

img = takeimage()
initp = findTankCentroid(img, "red")
time.sleep(1)
forward()
img = takeimage()
p = findTankCentroid(img, "red")

fac = -1
if initp[0] < p[0]:
    fac = +1

print(initp, p)
cv2.imwrite("cropped.png", img[p[0] - 25 : p[0] + 25, p[1] -25 : p[1] + 25])
m = lineFind(img[p[0] - 25 : p[0] + 25, p[1] -25 : p[1] + 25])
if m == 0.0:
    raytrace(img, p, [1 * fac, 0])
elif m == -0.0:
    raytrace(img, p, [1 * fac, -7 * fac])
else:
    if abs(1 / m) > 8:
        raytrace(img, p, [7*m * fac, -7*fac])
    else:
        raytrace(img, p, [1*fac, -1/m*fac])
