# -*- coding: utf-8 -*
from matplotlib import pyplot as plt
import numpy as np
import cv2
import random
import mathFunc as mfc
import copy

def showImg(img):
    cv2.namedWindow('Img')
    cv2.imshow('Img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
    dst = copy.deepcopy(block)
    noRow = block.shape[0]
    noCol = block.shape[1]
    for row in xrange(noRow):
        for col in xrange(noCol):
            dst[row, col] = dst[row, col] >> 1
            dst[row, col] = dst[row, col] << 1
    return dst

def xor(block, bitArray):
    bitBlock = mfc.reshape(bitArray, (block.shape[0], block.shape[1]))
    dst = np.bitwise_xor(block, bitBlock)
    return dst

def extractLSB(block):
    dst = copy.deepcopy(block)
    noRow = block.shape[0]
    noCol = block.shape[1]
    for row in xrange(noRow):
        for col in xrange(noCol):
            dst[row, col] = dst[row, col] & 1
    return dst

def binarize(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)#grayscale
    res = cv2.threshold(img, 127,1,cv2.THRESH_BINARY_INV)
    return res[1]

def replicate(img, size):#TODO
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
    row = 0
    col = 0
    blockSize = (blockLst[0].shape[0], blockLst[0].shape[1])
    #closure
    def newFill(row, col, d=dst):#start row and col
        def fill(block):
            blockH = blockSize[0]
            blockW = blockSize[1]
            for bRow in xrange(blockH):
                for bCol in xrange(blockW):
                    d[row+bRow, col+bCol] = block[bRow, bCol]
        return fill

    for block in blockLst:
        fill = newFill(row, col)
        fill(block)
        col += block.shape[1]
        if col >= size[1]:
            col = 0
            row += block.shape[0]
    return dst

def merge(chn, img):
    b, g, r = cv2.split(img)
    cv2.merge([b, chn, r], img)
    return img