# -*- coding: utf-8 -*
from matplotlib import pyplot as plt
import numpy as np
import cv2
import random
import mathFunc as mfc

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
        pass 
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
    LEN = 128#length of MD5(bits)
    size = mfc.getBlockSize(img.shape, LEN)
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
    g = cv2.split(img)[1]
    return g

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
    bitBlock = mfc.reshape(bitArray, (block.shape[0], block.shape[1]))
    dst = np.bitwise_xor(block, bitBlock)
    return dst

def extractLSB(block):
    noRow = block.shape[0]
    noCol = block.shape[1]
    for row in xrange(noRow):
        for col in xrange(noCol):
            val = block[row, col]
            val = val & 1
    return block

def binarize(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)#grayscale
    res = cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
    return res[1]

def replicate(img, size):
    res = createImg(size)
    for row in xrange(img.shape[0]):
        for col in xrange(img.shape[1]):
            res[row, col] = img[row, col]
            if (row+img.shape[0]) <= res.shape[0]:
                res[row+img.shape[0], col] = img[row, col]
            if (col+img.shape[1]) <= res.shape[1]:
                res[row, col+img.shape[1]] = img[row, col]
            if (row+img.shape[0]) <= res.shape[0] and (row+img.shape[0]) <= res.shape[0]:                
                res[row+img.shape[0], col+img.shape[1]] = img[row, col]            
    return res

def insert2LSB(block, bitmap):
    noRow = block.shape[0]
    noCol = block.shape[1]
    for row in xrange(noRow):
        for col in xrange(noCol):
            block[row, col] += bitmap[row, col]
    return block

def assembleBlocks(blockLst, size):   
    dst = createImg(size)
    row, col = 0
    for block in blockLst:
        noRow = block.shape[0]
        noCol = block.shape[1]
        for brow in xrange(noRow):
            for bcol in xrange(noCol):
                dst[row+brow, col+bcol] = block[brow, bcol]
        row += noRow
        col += noCol
        if row >= size[0] or col >= size[1]:
            break
    return dst