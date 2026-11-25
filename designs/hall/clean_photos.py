"""Soften a person's reflection in the dining-kitchen photo locally, before sending.

Usage: python3 clean_photos.py DINING_KITCHEN_PHOTO OUT_DIR

DINING_KITCHEN_PHOTO is IMG_8791 (kitchen opening in the middle, 2576x1932); a
faint reflection of a person in the dark glossy kitchen tiles is softened. The
living corner photo and the dining-end photo (IMG_8793) need no cleanup.
Coordinates fit the original 2576x1932 photo only.
Needs: pip install opencv-python-headless
"""
import sys
from pathlib import Path

import cv2
import numpy as np

dining_src, out_dir = sys.argv[1], Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

img2 = cv2.imread(dining_src)
assert img2 is not None and img2.shape[:2] == (1932, 2576), "expected the original 2576x1932 dining photo"
mask = np.zeros(img2.shape[:2], np.uint8)
cv2.rectangle(mask, (1305, 665), (1390, 840), 255, -1)
o2 = cv2.inpaint(img2, cv2.dilate(mask, np.ones((9, 9), np.uint8)), 10, cv2.INPAINT_TELEA)
cv2.imwrite(str(out_dir / "dining_clean.jpg"), o2, [cv2.IMWRITE_JPEG_QUALITY, 93])
print("wrote", out_dir / "dining_clean.jpg")
