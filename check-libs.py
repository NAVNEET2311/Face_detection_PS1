import cv2
import numpy as np
import torch
from skimage.metrics import structural_similarity as compare_ssim
import matplotlib.pyplot as plt

# Check versions
cv_version = cv2.__version__
np_version = np.__version__
torch_version = torch.__version__

cv_version, np_version, torch_version