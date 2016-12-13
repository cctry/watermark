# -*- coding: utf-8 -*
from matplotlib import pyplot as plt
import numpy as np
import cv2
import random
import mathFunc

def showImg(img, flag = 0):
    if img.ndim == 3:
        img = BGR2RGB(img)
    plt.imshow(img)
    if flag == 0:
        plt.xticks([]),plt.yticks([]) #隐藏坐标线 
    plt.show()

def createImg(shape, typeNum = 8):#[height, width]
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
    for k in xrange(n):
        if seed == 0:
            i = int(random.random() * img.shape[1])
            j = int(random.random() * img.shape[0])
        else:
            i = int(random.random(seed) * img.shape[1])
            j = int(random.random(seed) * img.shape[0])
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

def splitImg(img):#from left to right; from top to down
    height = img.shape[0]
    width = img.shape[1]
    LEN = 128#length of MD5
    size = mathFunc.getBlockSize(img.shape, LEN)
    hNum = height/size[0]
    wNum = width/size[1]
    res = list()
    for i in xrange(hNum):
        for j in xrange(wNum):
            startRow = 0 + i*size[0]
            endRow = size[0] + i*size[0]
            startCol = 0 + j*size[1]
            endCol = size[1] + j*size[1]
            block = img[startRow:endRow, startCol:endCol]
            res.append(block)
    return res
    
def getGChn(img):
    b = cv2.split(img)[1]
    return b

def zeroLSB(block):
    noRow = block.shape[0]
    noCol = block.shape[1]
    for row in xrange(noRow):
        for col in xrange(noCol):
            val = block[row, col]
            val = val >> 1
            val = val << 1
    return block

def xor(block, bitArray):
    bitBlock = mathFunc.reshape(bitArray)
    dst = np.bitwise_xor(block, bitArray)
    return dst

def extractLSB(block):
    noRow = block.shape[0]
    noCol = block.shape[1]
    for row in xrange(noRow):
        for col in xrange(noCol):
            val = block[row, col]
            var = val & 1
    return block
