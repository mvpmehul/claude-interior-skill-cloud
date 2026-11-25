"""Remove people from the hall photos locally, before anything is sent to Google.

Usage: python3 clean_photos.py LIVING_PHOTO DINING_KITCHEN_PHOTO OUT_DIR

LIVING_PHOTO is IMG_8799 (sliding doors on the left, bedroom door on the right,
2576x1932); the man standing by the glass is rebuilt from the surrounding
glass, frame and wall. DINING_KITCHEN_PHOTO is IMG_8791 (kitchen opening in the
middle); a faint reflection of a person in the dark kitchen tiles is softened.
The dining-end photo (IMG_8793) needs no cleanup. Coordinates fit the original
2576x1932 photos only. Needs: pip install opencv-python-headless
"""
import sys
from pathlib import Path

import cv2
import numpy as np

living_src, dining_src, out_dir = sys.argv[1], sys.argv[2], Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)

img = cv2.imread(living_src)
assert img is not None and img.shape[:2] == (1932, 2576), "expected the original 2576x1932 living photo"
img = img.astype(np.float32)
out = img.copy()
y1, y2 = 690, 1125
out[y1:y2, 716:792] = img[y1:y2, 636:712]                      # glass pane, one pane to the left
for c0, c1 in ((700, 716), (792, 824)):                          # mullion and door frame
    out[y1:1068, c0:c1] = img[660, c0:c1][None, :, :]
gain = img[y1 - 30:y1, 824:915].mean(axis=(0, 1)) / img[y1 - 30:y1, 924:1015].mean(axis=(0, 1))
out[y1:1062, 824:915] = img[y1:1062, 924:1015] * gain           # wall, brightness matched
out[1062:y2, 792:915] = img[1062:y2, 892:1015]                  # skirting and floor
o = np.clip(out, 0, 255).astype(np.uint8)
blur = cv2.GaussianBlur(o, (9, 9), 0)
band = np.zeros(o.shape[:2], bool)
for x in (716, 792, 824, 915):
    band[y1:y2, x - 4:x + 4] = True
band[y1 - 4:y1 + 4, 700:915] = True
band[1058:1066, 792:915] = True
band[y2 - 4:y2 + 4, 700:915] = True
o[band] = blur[band]
cv2.imwrite(str(out_dir / "living_clean.jpg"), o, [cv2.IMWRITE_JPEG_QUALITY, 93])

img2 = cv2.imread(dining_src)
assert img2 is not None and img2.shape[:2] == (1932, 2576), "expected the original 2576x1932 dining photo"
mask = np.zeros(img2.shape[:2], np.uint8)
cv2.rectangle(mask, (1305, 665), (1390, 840), 255, -1)
o2 = cv2.inpaint(img2, cv2.dilate(mask, np.ones((9, 9), np.uint8)), 10, cv2.INPAINT_TELEA)
cv2.imwrite(str(out_dir / "dining_clean.jpg"), o2, [cv2.IMWRITE_JPEG_QUALITY, 93])
print("wrote", out_dir / "living_clean.jpg", "and", out_dir / "dining_clean.jpg")
