#coding:utf-8
import cv2
import sys
from core import insert as st
from core import extract as xt
from utils import imageFunc as ifc
#main
if len(sys.argv) <= 1 or len(sys.argv) > 6:
    argError()
if sys.argv[1] == 'insert':
    img = cv2.imread(sys.argv[2], CV_LOAD_IMAGE_UNCHANGED)
    mark = cv2.imread(sys.argv[3], CV_LOAD_IMAGE_UNCHANGED)
    _insert(img, mark, key, flag)
    exit()
if sys.argv[1] == 'extract':
    img = cv2.imread(sys.argv[2], CV_LOAD_IMAGE_UNCHANGED)
    key = rsa.loadKey(sys.argv[3])
    if len(sys.argv) == 6:#full arg with path
        if sys.argv[4] != '-s':
            argError()
        path = sys.argv[5]        
        dst = _extract(img, key)
        cv2.imwrite(path+'extracted_'+sys.argv[2], dst)
    if len(sys.argv) == 5:#save without path
        if sys.argv[4] != '-s':
            argError()       
        dst = _extract(img, key)
        cv2.imwrite('extracted_'+sys.argv[2], dst)
    if len(sys.argv) == 4:#show the image
        dst = _extract(img, key)
        show(dst)
        exit()
else:
    argError()

#func
def error(func):
    def newFunc():
        func()
        exit()
    return newFunc

@error
def argError():
    print 'Please input the correct agruments'

def _insert(img, mark):
    return st.insert(img, mark)

def _extract(img, key):
    return xt.extract(img,key)

def show(img):
    ifc.showImg(img)