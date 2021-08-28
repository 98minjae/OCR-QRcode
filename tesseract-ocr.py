import cv2
import pytesseract
img=cv2.imread("blur.png")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey()

gray2=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU[1])
cv2.imshow("gray2", gray2)
cv2.waitKey()

gray3=cv2.medianBlur(gray2,3)
cv2.imshow("gray3", gray3)
cv2.waitKey()

ocr=pytesseract.image_to_string(img)
print(ocr)
