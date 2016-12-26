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

