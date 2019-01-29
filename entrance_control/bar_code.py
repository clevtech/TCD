import numpy as np
import cv2
import math
from scipy import ndimage
from pyzbar.pyzbar import ZBarSymbol
from pyzbar.pyzbar import decode


# cv2 and pyzbar libraries for python3 needed
# pip3 install opencv-python
# pip3 install pyzbar
def barcode_scan(path):
	img_before = cv2.imread(path)
	img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
	img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
	lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
	angles = []

	for x1, y1, x2, y2 in lines[0]:
		cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
		angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
		angles.append(angle)

	median_angle = np.median(angles)
	img_rotated = ndimage.rotate(img_before, median_angle)

	result = decode(img_rotated, symbols=[ZBarSymbol.CODE128])
	output_data = result[0][0]
	print(str(output_data)[1:])

barcode_scan('./static/udo.png')
