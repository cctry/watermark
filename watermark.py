#coding:utf-8
import cv2
import sys
from core import insert
from core import extract
from utils import imageFunc as ifc
from utils import rsa as RSA
#func
def error(func):
    def newFunc():
        func()
        exit()
    return newFunc

@error
def argError():
    print 'Please input the correct agruments'

def show(img):
    ifc.showImg(img)

#main
if len(sys.argv) <= 1 or len(sys.argv) > 6:
    argError()
if sys.argv[1] == 'insert':
    rsa = RSA.encryptor()
    img = cv2.imread(sys.argv[2], -1)
    mark = cv2.imread(sys.argv[3], -1)
    insert(img, mark)
    exit()
if sys.argv[1] == 'extract':
    rsa = RSA.encryptor()
    img = cv2.imread(sys.argv[2], -1)
    key = rsa.loadKey(sys.argv[3])
    if len(sys.argv) == 6:#full arg with path
        if sys.argv[4] != '-s':
            argError()
        path = sys.argv[5]        
        dst = extract(img, key)
        cv2.imwrite(path+'extracted_'+sys.argv[2], dst)
    if len(sys.argv) == 5:#save without path
        if sys.argv[4] != '-s':
            argError()       
        dst = extract(img, key)
        cv2.imwrite('extracted_'+sys.argv[2], dst)
    if len(sys.argv) == 4:#show the image
        dst = extract(img, key)
        show(dst)
        exit()
else:
    argError()
