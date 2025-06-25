# scripts/compare_images.py
import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim

def mse(imageA, imageB):
    return np.mean((imageA - imageB) ** 2)

def compare_images(img_path1, img_path2, resize_shape=(300, 300)):
    imageA = cv2.imread(img_path1)
    imageB = cv2.imread(img_path2)

    if imageA is None or imageB is None:
        raise FileNotFoundError("One or both image paths are invalid.")

    imageA = cv2.resize(imageA, resize_shape)
    imageB = cv2.resize(imageB, resize_shape)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    score, diff = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    # Convert grayscale diff to BGR for color image viewing
    diff_color = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)

    error = mse(grayA, grayB)

    return score, error, diff_color
