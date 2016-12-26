from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA
from preprocess import preprocess

def extract(img,key):
    testImg = copy.deepcopy(img)
    if testImg.ndim == 3：#colored
        testImg,img = ifc.getGChn(testImg)
    imgBlocks, size = ifc.splitImg(img)
    imgBlocks1 = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    imgBlocks2 = ifc.extractLSB(imgBlocks)
    rsa = RSA.rsa()
    imgBlocks3 = RSA.decrypt(key,imgBlocks2)
    blocks = list()
    for i in xrange(len(imgBlocks1)):
        imgBlock = imgBlocks1[i]
        hashBits = mfc.hash(testImg.shape[1], testImg.shape[0], imgBlocks1)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])
        bitmap = ifc.xor(imgBlocks3, hashBits)
        dst = ifc.assembleBlocks(bitmap, (testImg.shape[0], testImg.shape[1]))
    return dst