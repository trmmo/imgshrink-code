import cv2
import numpy as np


def compare_images(img1_path, img2_path, output_path, selection):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        print("Khong the doc anh!!")
        return

    if img1.shape != img2.shape:
        print("Hai anh khong cung kich thuoc!!")
        h = min(img1.shape[0], img2.shape[0])
        w = min(img1.shape[1], img2.shape[1])
        img1 = cv2.resize(img1, (w, h))
        img2 = cv2.resize(img2, (w, h))

    diff = np.zeros_like(img1)
    count = 0
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            # Lấy giá trị pixel
            b1, g1, r1 = img1[i, j]
            b2, g2, r2 = img2[i, j]
            if b1 == b2 and g1 == g2 and r1 == r2:
                diff[i, j] = [255,255,255]
            else:
                diff[i, j] = [255,0,255]
                count += 1

    diff_normalized = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
    if (selection == 1):
        print(f"2 anh khac nhau {count} diem anh")
    else:
        cv2.imwrite(output_path, diff_normalized)
        print(f"Anh so sanh duoc luu tai: {output_path}")


img_path1 = input("Nhap vi tri file anh 1: ")
img_path2 = input("Nhap vi tri file anh 2: ")
selection = int(input(
"""Nhap tuy chon:
    1: Dem so pixel khac nhau
    2: Xuat anh so sanh 2 anh
"""))

compare_images(img_path1, img_path2, "diff.jpg", selection)
