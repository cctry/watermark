from matplotlib import pyplot as plt
import numpy as np

def showImg(img, cls, flag):
    plt.imshow(img, cls) #必须规定为显示的为什么图像
    if flag == 0:
        plt.xticks([]),plt.yticks([]) #隐藏坐标线 
    plt.show()

def createImg(shape, typeNum):
    if isinstance(shape, tuple) is False:
        print "Wrong argument"
    types = (8, 16, 32, 64)
    if typeNum not in types:
        print "Wrong argument"
    if typeNum == 8:
        emptyImage = np.zeros(shape, np.uint8)
    elif typeNum == 16:
        emptyImage = np.zeros(shape, np.uint16)
    elif typeNum == 32:
        emptyImage = np.zeros(shape, np.uint32)
    elif typeNum == 64:
        emptyImage = np.zeros(shape, np.uint64)
    return emptyImage