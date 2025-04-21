import cv2
import numpy as np
path = input("Nhap duong dan file anh: ");
image = cv2.imread(path)

# Kích thước mới (ví dụ: 300x300)
width = image.shape[1]
height = image.shape[0]
# print(width,height)
# Resize ảnh
# print(image.shape)
resized_image = cv2.resize(image, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_LINEAR)
resized_image = cv2.resize(image, (width, height), interpolation = cv2.INTER_LINEAR)
#
# # Hiển thị ảnh gốc và ảnh đã resize
# # cv2.imshow('Original Image', image)
# # cv2.imshow('Resized Image', resized_image2)
path_out = "resized_image.jpg"
cv2.imwrite(filename=path_out, img=resized_image2)
print("Chinh sua anh thanh cong! Duong dan file: " + path_out)

