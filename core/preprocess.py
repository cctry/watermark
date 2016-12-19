from utils import imageFunc as ifc
import cv2

def preprocess(img, mark, flag):#if colered image, flag == 1  
    if flag == 1:#extract green channel
        green = mfc.getGChn(img)    
        mark = _markProcess(mark)
    if mark.shape == img.shape:
        pass
    elif img.shape[0]*img.shape[1] >= mark.shape[0]*mark.shape[1]:
        mark = _replicate(mark, img.shape)
    else：
        mark = _cutImg(img, img.shape)：
    return img, green, mark
#utils
def _markProcess(img):
    return mfc.binarize(img)

def _replicate(img, size):
    return mfc.replicate(img, size)

def _cutImg(img, size):
    return img[0:size[0], 0:size[1]]
