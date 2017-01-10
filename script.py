import numpy as np
from skimage.io import imread, imsave


def step1(image, rad_mult, rad_add):
    nimg = image.copy()
    nimg *= rad_mult
    nimg += rad_add
    return nimg

def step2(image, LU, LD, T, e):
    nimg = image.copy()
    part = LU - (1 - e)*LD
    nimg -= part
    nimg /= (T*e)
    return nimg

if __name__ == '__main__':
    __IMG_PATH = 'LT52200762000296CUB00_B6.TIF'
    __RAD_MULT = 0.0553
    __RAD_ADD = 1.256
    __LU = 1
    __LD = 2
    __T = 3
    __E = 4
    img = imread(__IMG_PATH)
    img = img.astype("float64")
    tmp_img = step1(img, __RAD_MULT, __RAD_ADD)
    tmp_img = step2(tmp_img, __LU, __LD, __T, __E)

