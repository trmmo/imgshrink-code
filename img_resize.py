import cv2
import argparse
import hashlib


def hashCal(path, algo='md5'):
    hasher = hashlib.new(algo)

    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pathin', default="fakepathin.jpg", type=str, help='Duong dan anh input')
    parser.add_argument('--pathout', default="fakepathout.jpg", type=str, help='Duong dan anh output')
    parser.add_argument('--width', default=100, type=int, help='Chieu ngang anh')
    parser.add_argument('--height', default=100, type=int, help='Chieu cao anh')
    args = parser.parse_args()

    image = cv2.imread(args.pathin)
    width = image.shape[1]
    height = image.shape[0]
    resized_image = cv2.resize(cv2.resize(image, (args.width, args.height)), (width, height))

    cv2.imwrite(filename=args.pathout, img=resized_image)
    hash_value = hashCal(args.pathout)
    print(f"Anh moi luu tai: {args.pathout}, MD5 checksum: {hash_value}")
