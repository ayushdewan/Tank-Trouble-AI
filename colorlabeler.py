import numpy as np
import cv2

bounds = {
	"red" : (np.array([120, 75, 75]), np.array([130, 255, 255])),
	"blue" : (np.array([110, 75, 75]), np.array([130, 255, 255])),
	"green" : (np.array([35, 0, 0]), np.array([85, 255, 255])),
	"yellow" : (np.array([20, 75, 75]), np.array([40, 255, 255])),
	"white" : (np.array([0, 0, 20]), np.array([180, 30, 255])),
	"orange" : (np.array([10, 100, 100]), np.array([20, 255, 255]))
}

def findTankCentroid(img, color = "green"):
	lower = bounds[color][0]
	upper = bounds[color][1]
	mask = cv2.inRange(cv2.cvtColor(img, cv2.COLOR_RGB2HSV), lower, upper)
	x = 0
	y = 0
	num_hits = 0
	for i in range(len(mask)):
		for j in range(len(mask[0])):
			if mask[i][j] > 0:
				x += i
				y += j
				num_hits += 1
	mask[int(x / num_hits)][int(y / num_hits)] = 150
	cv2.imwrite("yo.png", mask)
	return (int(x / num_hits), int(y / num_hits))
