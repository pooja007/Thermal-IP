import cv2
import numpy as np 
import scipy

img = cv2.imread('test9.png',1)

print img.shape # (y,x, channels) ie (ht,width,channels)
print img.size
print img.dtype

b,g,r = cv2.split(img)

gray = np.zeros(img.shape, np.uint8)

#i,j = scipy.where(r<5 & g<5)
#print i,j

#if (g[i,j] < 5):
#gray[i,j] = (b[i,j] -150 )*(255/950)

#if (b[i,j] > 250):
#	gray[i,j] = 100*255/950 + g[i,j] * 255/950

#print len(i)

# we need to optimise it using numpy functions that i'm unable to  :/ I'll check soon. but for now double for loops

print 'hello'
'''
for i in range(0,img.shape[0]):
	for j in range(0,img.shape[1]):
		if (r[i,j] < 5):
			if (g[i,j] <5):
				gray[i,j] = b[i,j]*255/950- 130*255/950
				#print 'b' 
				#print b[i,j]
				#print 'gval' 
				#print g[i,j]
			elif (b[i,j]> 250):
				gray[i,j] = 100*255/950 + g[i,j] * 255/950

		if(g[i,j]>250):
			gray[i,j] = r[i,j]*255/950+ 100*255/950 + 250 *255/950 

		if(b[i,j]<5):
			if(r[i,j]>250):
				gray[i,j] = 600* 255/950 + 250*255/950 -g[i,j]*255/950
			elif(g[i,j]<5):
				gray[i,j] = 850*255/950 + (250- r[i,j]) * 255/950

'''
'''
for i in range(0,img.shape[0]):
	for j in range(0,img.shape[1]):
		if (r[i,j] <=3):
			if (g[i,j] <=3):
				gray[i,j] = b[i,j]*255/950- 130*255/950
				#print 'b' 
				#print b[i,j]
				#print 'gval' 
				#print g[i,j]
			elif (b[i,j]>= 250):
				gray[i,j] = 100*255/950 + g[i,j] * 255/950

		if(g[i,j]>=250):
			gray[i,j] = r[i,j]*255/950+ 100*255/950 + 250 *255/950 

		if(b[i,j]<=3):
			if(r[i,j]>=250):
				gray[i,j] = 600* 255/950 + 250*255/950 -g[i,j]*255/950
			elif(g[i,j]<=3):
				gray[i,j] = 850*255/950 + (250- r[i,j]) * 255/950

'''

for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			if (r[i,j] <=15):
				if (g[i,j] <=15):
					gray[i,j] = b[i,j]*255/950- 130*255/950
					
				elif (b[i,j]>= 250):
					gray[i,j] = 100*255/950 + g[i,j] * 255/950

			if(g[i,j]>=250):
				gray[i,j] = r[i,j]*255/950+ 100*255/950 + 250 *255/950 

			if(b[i,j]<=15):
				if(r[i,j]>=250):
					gray[i,j] = 600* 255/950 + 250*255/950 -g[i,j]*255/950
				elif(g[i,j]<=15):
					gray[i,j] = 850*255/950 + (250- r[i,j]) * 255/950


kernel = np.ones((3,3),np.uint8)

dilation = cv2.dilate(gray,kernel,iterations = 1)
graynew = cv2.erode(dilation,kernel,iterations = 1)

#print img.shape[1]

# fine tune the image by converting into float and also using numpys. 

#cv2.namedWindow('b',cv2.WINDOW_NORMAL)
#cv2.namedWindow('g',cv2.WINDOW_NORMAL)
#cv2.namedWindow('r',cv2.WINDOW_NORMAL)
cv2.namedWindow('gray',cv2.WINDOW_NORMAL)

cv2.namedWindow('thresh',cv2.WINDOW_NORMAL)

#cv2.namedWindow('graynew',cv2.WINDOW_NORMAL)

cv2.imshow('gray',gray)
#cv2.imshow('graynew',graynew)

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)

cv2.imshow('thresh',thresh)

#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)

cv2.imwrite('test9_big.jpg',gray)
#cv2.imwrite('test4.2_new.jpg',graynew)

cv2.namedWindow('just',cv2.WINDOW_NORMAL)

cv2.imshow('just',img)
cv2.waitKey(0)

cv2.destroyAllWindows()