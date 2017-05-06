import cv2

img = cv2.imread('test5_small.jpg',0)

ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('lol',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()