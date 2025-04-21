import cv2
import numpy as np


def compare_images(img_path1, img_path2):
    # Đọc hai ảnh
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    # Kiểm tra xem ảnh có tồn tại không
    if img1 is None or img2 is None:
        print("❌ Một trong hai ảnh không tồn tại hoặc không thể đọc.")
        return

    # Resize ảnh về cùng kích thước nếu cần (tùy chọn)
    if img1.shape != img2.shape:
        print("⚠️ Hai ảnh có kích thước khác nhau, sẽ được resize ảnh thứ hai.")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # So sánh điểm ảnh (theo từng kênh màu)
    difference = cv2.absdiff(img1, img2)
    gray_diff = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    # Nếu không có khác biệt thì tất cả pixel sẽ là 0
    if np.count_nonzero(gray_diff) == 0:
        print("✅ Hai ảnh giống nhau hoàn toàn.")
    else:
        print("❌ Hai ảnh khác nhau.")
        print(np.count_nonzero(gray_diff))
        # Hiển thị vùng khác biệt
        cv2.imshow("Khác biệt", difference)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def compare_pixel_by_pixel(img1_path, img2_path, output_path):
    # Đọc 2 ảnh
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Kiểm tra nếu ảnh không tồn tại
    if img1 is None or img2 is None:
        print("Không thể đọc ảnh")
        return

    # Đảm bảo 2 ảnh cùng kích thước
    if img1.shape != img2.shape:
        print("Hai ảnh có kích thước khác nhau, tiến hành resize")
        h = min(img1.shape[0], img2.shape[0])
        w = min(img1.shape[1], img2.shape[1])
        img1 = cv2.resize(img1, (w, h))
        img2 = cv2.resize(img2, (w, h))

    # Tạo ảnh kết quả (khác biệt)
    diff = np.zeros_like(img1)

    # So sánh từng pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            # Lấy giá trị pixel
            b1, g1, r1 = img1[i, j]
            b2, g2, r2 = img2[i, j]
            if b1==b2 and g1 == g2 and r1==r2:
            # Tính độ khác biệt (có thể dùng cách khác)
                diff[i, j] = [255,255,255]
            else:
                diff[i, j] = [0,0,255]

    # Chuẩn hóa ảnh diff để hiển thị rõ hơn
    diff_normalized = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)

    # Tạo ảnh kết quả tổng hợp (3 ảnh ngang hàng)
    result = np.hstack((img1, img2, diff_normalized))

    # Lưu ảnh kết quả
    cv2.imwrite(output_path, diff_normalized)

    # Hiển thị ảnh (tuỳ chọn)
    cv2.imshow("",diff_normalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img_path1 = input("Nhập đường dẫn ảnh 1: ")
img_path2 = input("Nhập đường dẫn ảnh 2: ")
# compare_images(img_path1, img_path2)
compare_pixel_by_pixel(img_path1, img_path2, "out_img.jpg")
