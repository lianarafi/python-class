import cv2
import cvzone
#first image
image=cv2.imread(r"C:\Users\Rafie\Desktop\IMG_20231012_133332_868.jpg")
image=cv2.resize(image,(450,600))
image=cv2.rectangle(image,(350,170),(190,320),(40,133,57),5)
image=image[170:320,190:350]
cv2.imwrite(r"C:\Users\Rafie\Downloads\liana.jpg",image)
#secend image
img=cv2.imread(r"D:\IMG_20231012_133329_885.jpg")
img=cv2.resize(img,(450,600))
img=cv2.rectangle(img,(360,170),(190,320),(50,133,57),5)
img=img[170:320,190:360]
cv2.imwrite(r"c:\Users\Rafie\Downloads\lili.jpg",img)
#third image
img2=cv2.imread(r"D:\IMG_20231012_133334_823.jpg")
img2=cv2.resize(img2,(450,600))
img2=cv2.rectangle(img2,(310,140),(190,320),(50,133,57),5)
img2=img2[140:320,190:310]
cv2.imwrite(r"C:\Users\Rafie\Downloads\lil.jpg",img2)
cv2.imshow('photo',image)
cv2.imshow('lili',img)
cv2.imshow('lil',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



