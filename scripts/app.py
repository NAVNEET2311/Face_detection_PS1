# scripts/app.py
import cv2
from matplotlib import pyplot as plt
from compare_images import compare_images
from detect_objects import detect_with_haar

def run(image1, image2, use_yolo=True):
    # Step 1: Compare
    ssim_score, mse_score, diff_img = compare_images(image1, image2)

    # Step 2: Object Detection
    detection1 = detect_with_haar(image1)
    detection2 = detect_with_haar(image2)

    # Step 3: Display
    print(f"[SSIM Score] {ssim_score:.4f}")
    print(f"[MSE] {mse_score:.2f}")

    cv2.imshow("Diff Image", diff_img)
    cv2.imshow("Detected 1", cv2.imread(str(detection1)))
    cv2.imshow("Detected 2", cv2.imread(str(detection2)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
