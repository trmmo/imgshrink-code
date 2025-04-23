import cv2

path_in = input("Nhap duong dan file anh: ")
image = cv2.imread(path_in)

width = image.shape[1]
height = image.shape[0]

resized_image = cv2.resize(cv2.resize(image, (int(width / 2), int(height / 2))), (width, height))

path_out = "attacked.jpg"
cv2.imwrite(filename=path_out, img=resized_image)
print(f"Da sua anh, duong dan file: {path_out}")
