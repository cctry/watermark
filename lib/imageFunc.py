from matplotlib import pyplot as plt
import numpy as np

def showImg(img, flag):
    #plt.imshow(img, cls) #必须规定为显示的为什么图像
    plt.imshow(img)#require test
    if flag == 0:
        plt.xticks([]),plt.yticks([]) #隐藏坐标线 
    plt.show()

def createImg(shape, typeNum):
    if isinstance(shape, tuple) is False:
        print "Wrong argument"#TODO exception
    types = (8, 16, 32, 64)
    if typeNum not in types:
        print "Wrong argument"#TODO exception
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
            i = int(random.seed() * img.shape[1])
            j = int(random.seed() * img.shape[0])
        elif:
            i = int(random.seed(seed) * img.shape[1])
            j = int(random.seed(seed) * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img
