import os
import cv2
import numpy as np

src_dir = "./IconSet/AllCountries"
dst_dir = "./IconSet/AllCountries-144"
os.makedirs(dst_dir, exist_ok=True)

countries_png = os.listdir(src_dir)
for country_name in countries_png:
    country_name = country_name.split(".")[0]
    ori_img = cv2.imread(src_dir + "/" + country_name + ".png", cv2.IMREAD_UNCHANGED)
    # 设定一个 144 * 144 的画布 将图像缩放后放置在中心
    img = np.zeros((144, 144, 4), dtype=np.uint8)
    h, w = ori_img.shape[:2]
    if h > w:
        scale = 144 / h
        new_w = int(w * scale)
        ori_img = cv2.resize(ori_img, (new_w, 144))
        x = (144 - new_w) // 2
        img[:, x:x+new_w] = ori_img
    else:
        scale = 144 / w
        new_h = int(h * scale)
        ori_img = cv2.resize(ori_img, (144, new_h))
        y = (144 - new_h) // 2
        img[y:y+new_h, :] = ori_img
    cv2.imwrite(dst_dir + "/" + country_name + ".png", img)
print("144x144 image has been generated successfully!")