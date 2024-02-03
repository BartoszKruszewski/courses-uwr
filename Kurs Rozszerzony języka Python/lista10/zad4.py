import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

'''
Rezulaty dzialania programu nie sa najladniejsze,
ale wykorzystuja numpy oraz spelniaja warunki zadania.
'''

def is_gray(img):
    E = 0.08
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()
    return np.logical_and(abs(r - g) < E, abs(r - b) < E, abs(g - b) < E)

def get_mask(img, cords):
    SHIFT = 70

    colors = img.copy()
    colors[cords] = 0

    mask = colors.copy()
    mask = np.where(mask == 0, np.roll(colors, SHIFT, axis=0), mask)
    mask = np.where(mask == 0, np.roll(colors, -SHIFT, axis=0), mask)
    mask = np.where(mask == 0, np.roll(colors, SHIFT, axis=1), mask)
    mask = np.where(mask == 0, np.roll(colors, -SHIFT, axis=1), mask)

    return mask

img = mpimg.imread("image.png")
org_img = img.copy()
happy_img = img.copy()
sad_img = img.copy()

gray_cords = is_gray(img)
not_gray_cords = np.logical_not(gray_cords)

happy_img[gray_cords] = get_mask(img, gray_cords)[gray_cords]
sad_img[not_gray_cords] = get_mask(img, not_gray_cords)[not_gray_cords]

plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(org_img)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Happier')
plt.imshow(happy_img)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Sadder')
plt.imshow(sad_img)
plt.axis('off')

plt.show()