import nltk
from nltk import word_tokenize
import cv2
doc=open('output.txt')
d=doc.read()
corpus=d.split()
#print(corpus)

im = cv2.imread('10.1.1.1.2004_4.tif')
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_, contours,hierarchy =cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    roi=im[y:y+h,x:x+w]
    #print(roi)
    #cv2.imwrite(str(idx) + '.tif', roi)
    cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)
    print(x)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
imS = cv2.resize(im, (6000,6000 ))                    # Resize image
cv2.imshow("output", imS)                            # Show image
cv2.waitKey(0)   
