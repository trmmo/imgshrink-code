import cv2
import numpy as np
import argparse
import hashlib


def hashCal(path, algo='md5'):
    hasher = hashlib.new(algo)

    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def export_diff(img1_path, img2_path, output_path):
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
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            b1, g1, r1 = img1[i, j]
            b2, g2, r2 = img2[i, j]
            if b1 == b2 and g1 == g2 and r1 == r2:
                diff[i, j] = [255, 255, 255]
            else:
                diff[i, j] = [0, 0, 255]

    diff_normalized = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(output_path, diff_normalized)
    hash_value = hashCal(output_path)
    print(f"Anh so sanh duoc luu tai: {output_path}, MD5 checksum: {hash_value}")


def count_diff(img1_path, img2_path):
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

    count = 0
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            b1, g1, r1 = img1[i, j]
            b2, g2, r2 = img2[i, j]
            if not (b1 == b2 and g1 == g2 and r1 == r2):
                count += 1
    print(f"Hai anh khac nhau {count} pixel.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path1', default="fakepath1.jpg", type=str, help='Duong dan anh 1')
    parser.add_argument('--path2', default="fakepath2.jpg", type=str, help='Duong dan anh 2')
    parser.add_argument('--pathout', default="fakepathout.jpg", type=str, help='Duong dan anh 2')
    parser.add_argument('--action', default="nothing", type=str, help='Duong dan anh 2')
    args = parser.parse_args()

    if args.action == "export":
        export_diff(args.path1, args.path2, args.pathout)
    elif args.action == "count":
        count_diff(args.path1, args.path2)
    else:
        print("Success is not final, failure is not fatal: it is the courage to continue that counts. :D")
