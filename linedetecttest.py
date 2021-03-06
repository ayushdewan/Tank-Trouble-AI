import cv2
import numpy as np
import matplotlib.pyplot as plt
import keyboard

def lineFind(img):
    #img = cv2.imread("meme.png")
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)


    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)


    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 10  # minimum number of pixels making up a line
    max_line_gap = 20  # maximum gap in pixels between connectable line segments
    line_image = np.copy(img) * 0  # creating a blank to draw lines on

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)



    import math
    minLength = [1000000.0, 0]
    for line in lines:
        for x1,y1,x2,y2 in line:
            plt.plot([x1,x2],[y1,y2])
            mag = math.hypot(x1-x2, y1-y2)
            print(mag)
            if mag < minLength[0]:
                if y2 - y1 == 0:
                    minLength = [mag, 7]
                else:
                    minLength = [mag, float(x2 - x1) / float(y2 - y1)]

            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

    lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)



    cv2.imwrite("skrrr.png", lines_edges)
    #plt.show()
    return minLength[1]

def valid(x, y, w, h):
    return (0 <= x < w) and (0 <= y < h)

def raytrace(img, p, d):
    cv2.circle(img, (10,0), 3, (0, 255, 0, 255), -1)
    curr = [p[1], p[0]]
    pix = np.array([77, 77, 77, 255])
    walls = cv2.inRange(img, pix, pix)
    for i in range(200):
        intcurr = (int(curr[0]), int(curr[1]))
        if walls[intcurr[1]][intcurr[0]] > 0:
            if (valid(intcurr[1] + 10, intcurr[0], 690, 430) and walls[intcurr[1]][intcurr[0]+10]>0) or (valid(intcurr[1] - 10, intcurr[0], 690, 430) and walls[intcurr[1]][intcurr[0]-10]>0):
                d = [-d[0], d[1]]
                curr = [curr[0] + d[1], curr[1] + d[0]]
                intcurr = (int(curr[0]), int(curr[1]))
                if walls[intcurr[1]][intcurr[0]] > 0:
                    d = [-d[0], -d[1]]
                    curr = [curr[0] + d[1], curr[1] + d[0]]
                    intcurr = (int(curr[0]), int(curr[1]))
            else:
                d = [d[0], -d[1]]
                curr = [curr[0] + d[1], curr[1] + d[0]]
                intcurr = (int(curr[0]), int(curr[1]))
                if walls[intcurr[1]][intcurr[0]] > 0:
                    d = [-d[0], -d[1]]
                    curr = [curr[0] + d[1], curr[1] + d[0]]
                    intcurr = (int(curr[0]), int(curr[1]))


        #cv2.circle(img, intcurr, 3, (0, 255, 0, 255), -1)
        # keyboard.forward()
        img[intcurr[1]][intcurr[0]] = np.array([0, 255, 255, 255])
        curr = [curr[0] + d[1], curr[1] + d[0]]
    cv2.imwrite("ray.png", img)
    return img
