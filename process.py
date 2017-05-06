import numpy as np
import cv2

img = cv2.imread('test5_big.jpg',0)
img2 = cv2.imread('test5_big.jpg')

ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(thresh,kernel,iterations = 1)
newimg = cv2.erode(dilation,kernel,iterations = 1)

newimg1 = newimg
contours,hierarchy = cv2.findContours(newimg1, 1, 2)

cnt = contours[54] 
#for test 5
area = cv2.contourArea(cnt)
for i in range(0,len(contours)):
	cnt = contours[i]
	area = cv2.contourArea(cnt)
	print 'area',i,area


#cv2.drawContours(img, contours, 65, (0,255,255), 3)
#for test 2
cv2.drawContours(img2, [cnt], 0, (0,255,255), 3)
#cv2.drawContours(img2, contours, 228, (100,255,0), 3)
#cv2.drawContours(img2, contours, 230, (0,255,0), 3)
#cv2.drawContours(img2, contours, 117, (0,255,111), 3)

#biggest is 294 which is the last one :P
epsilon = 0.01*cv2.arcLength(contours[54],True)
approx = cv2.approxPolyDP(contours[54],epsilon,True)

print 'area' , area
print 'number of contours',len(contours)
print 'approx',type(approx), approx.shape
print '---------------------------------------'
print len(approx)
print 'img',type(img), img.shape

print 'newimage type' , type(newimg), newimg.shape
#cv2.namedWindow('final',cv2.WINDOW_NORMAL)
#cv2.namedWindow('just',cv2.WINDOW_NORMAL)
#cv2.namedWindow('thres',cv2.WINDOW_NORMAL)
cv2.namedWindow('imaeb',cv2.WINDOW_NORMAL)
cv2.drawContours(img2, [approx], 0, (255,255,0), 3)
#cv2.imshow('final',approx)
cv2.imshow('newimg',newimg)
cv2.imshow('thres',thresh)
cv2.imshow('imaeb',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()