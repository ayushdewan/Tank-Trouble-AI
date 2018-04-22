import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2
from PIL import Image
from colorlabeler import findTankCentroid
from linedetecttest import lineFind, raytrace
from keyboard import shoot


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
p = findTankCentroid(img, "red")
print(p)
cv2.imwrite("cropped.png", img)
m = lineFind(img[p[0] - 25 : p[0] + 25, p[1] -25 : p[1] + 25])
print(m, "nfn")
if m == 0.0:
    raytrace(img, p, [-1, 0])
elif m == -0.0:
    raytrace(img, p, [-1, 7])
else:
    if abs(1 / m) > 8:
        raytrace(img, p, [-7*m, 7])
    else:
        raytrace(img, p, [-1, 1/m])
shoot()
