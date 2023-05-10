import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread('cars.jpeg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im,bbox,label,conf)
cc = cv2.cvtColor(output_image,cv2.COLOR_BGR2RGB)
plt.imshow(cc,)
plt.show()
print('Number of cars in the image is ' + str(label.count('cars')))