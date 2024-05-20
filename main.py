import cv2

img = cv2.imread('Picture/download.jpeg')
# print(img.shape)
width=int(img.shape[1]/5)
height =int(img.shape[0]/5)

scaled_img=cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
cv2.imwrite('scaled_photo1.jpg', scaled_img)
