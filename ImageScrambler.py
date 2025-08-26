import numpy as np
from PIL import Image
import random

# Read an image
img = Image.open('image.png')

# Convert the image to numpy array
orig = np.array(img)
copy=np.zeros_like(orig)

# Height and width of image in pixels
h=copy.shape[0]
w=copy.shape[1]

# Number of sectors to divide the image
blocks_ver=8
blocks_hor=8
print(h,w)

# (Must be divisible)
assert h%blocks_ver==0
assert w%blocks_hor==0

# Height and width of each sector
block_h=h//blocks_ver
block_w=w//blocks_hor

# New location of each sector in (row, col) coordinates
sectors=[(i,j) for i in range(blocks_hor) for j in range(blocks_ver)]
random.seed(0)
random.shuffle(sectors)

# For each sector, copy pixels of the image to the new location
for idx,sector in enumerate(sectors):
    sector_row=sector[1]
    sector_col=sector[0]
    orig_offset_row=sector_row*block_h
    orig_offset_col=sector_col*block_w
    
    offset_sector_row,offset_sector_col=divmod(idx,blocks_hor)
    offset_row=offset_sector_row*block_h
    offset_col=offset_sector_col*block_w
    
    for i in range(block_h):
        for j in range(block_w):
            copy[i+offset_row][j+offset_col]=orig[i+orig_offset_row][j+orig_offset_col]

# Convert the numpy array to an image
img = Image.fromarray(np.uint8(copy))

# Save the image
img.save('image_scrambled.png')

