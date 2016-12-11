# -*- coding: utf-8 -*
from matplotlib import pyplot as plt
import numpy as np
import cv2

def showImg(img, flag = 0):
    img = BGR2RGB(img)
    plt.imshow(img)#会变色 要改成RGB
    if flag == 0:
        plt.xticks([]),plt.yticks([]) #隐藏坐标线 
    plt.show()

def createImg(shape, typeNum):
    if isinstance(shape, tuple) is False:
        pass #TODO exception
    types = (8, 16, 32, 64)
    if typeNum not in types:
        pass #TODO exception
    if typeNum == 8:
        emptyImage = np.zeros(shape, np.uint8)
    elif typeNum == 16:
        emptyImage = np.zeros(shape, np.uint16)
    elif typeNum == 32:
        emptyImage = np.zeros(shape, np.uint32)
    elif typeNum == 64:
        emptyImage = np.zeros(shape, np.uint64)
    return emptyImage

def salt(img, n, seed = 0):#在随机n个点添加噪声
    for k in range(n):
        if seed == 0:
            i = int(np.random.random(seed) * img.shape[1])#随机数处理有问题TODO
            j = int(np.random.random(seed) * img.shape[0])
        else:
            i = int(np.random.random(seed) * img.shape[1])
            j = int(np.random.random(seed) * img.shape[0])
        if img.ndim == 2:#为灰度图时
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img

def BGR2RGB(img):
    b, g, r = cv2.split(img)
    dst = cv2.merge([r, g, b])
    return dst

