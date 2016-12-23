#coding:utf-8
import cv2
import sys
from core import insert as is
from core import extract as xt
if len(sys.argv) <= 1 or len(sys.argv) > 6:
    inputError()

if sys.argv[1] == 'insert':
    if len(sys.argv) == 4:
        img = cv2.imread(sys.argv[2], CV_LOAD_IMAGE_UNCHANGED)
        mark = cv2.imread(sys.argv[3], CV_LOAD_IMAGE_UNCHANGED)
        if len(img.shape) == 1:
            flag = 0
        if len(img.shape) == 3:
            flag = 1
        _insert(img, mark, key)
def error(func):
    def newFunc():
        func()
        exit()
    return newFunc

@error
def inputError():
    print 'Please input the correct agruments'

def _insert(img, mark, key):
    return is.insert(img, mark, key)