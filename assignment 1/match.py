import cv2
import cvzone
face=cv2.imread(r"D:\IMG_20231012_133327_774.jpg")
face=cv2.resize(face,(250,400))
face2=cv2.imread(r"C:\Users\Rafie\Downloads\lili.png",cv2.IMREAD_UNCHANGED)
face2=cv2.resize(face2,(50,100))
img=face[50:100,60:200]
face[170:320,190:350]=cvzone.overlayPNG(img,face2)
cv2.imwrite(r"C:\Users\Rafie\Downloads\lil.jpg",face)
cv2.imshow("lilii",face)
cv2.waitKey(0)
 