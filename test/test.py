# -*- coding: utf-8 -*
from core import insert as st
from core import extract as xt
from utils import imageFunc as ifc
import numpy as np
import cv2
#main
def scaleImg(img,rowMul,colMul):#The zoom in and out of the image
    
   

def rotateImg(img):#The rotation of the image 
    imgBlocks,img.shape = ifc.splitImg(img)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imwrite(instextImg,dst)
    cv2.ShowImage(dst)
    return dst 


def compressImg(img,):#The compression of the image 


def instextImg(img,xPos,yPos,text):#Insert text to the image
    imgBlocks,img.shape = ifc.splitImg(img)
    font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
    y = img.shape[0]/ 2 
    x = img.shape[1] / 4 
    dst = cv2.PutText(image,"text", (x,y),font, cv.RGB(255, 255, 255))
    cv2.imwrite(instextImg,dst)
    cv2.ShowImage('text', dst) #Show the image
    return dst

def addSalt(img, n, seed = 0):#在随机n个点添加噪声
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
