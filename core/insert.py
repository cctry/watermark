from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA
from preprocess import preprocess
import copy

def insert(img, mark):
    oriImg = copy.deepcopy(img)
    if oriImg.ndim == 3:#colored
        img = ifc.getGChn(oriImg)
    mark = preprocess(img, mark)
    imgBlocks = ifc.splitImg(img)
    markBlocks = ifc.splitImg(mark)
    imgBlocks = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    blocks = list()
    for i in xrange(len(imgBlocks)):
        imgBlock = imgBlocks[i]
        markBlock = markBlocks[i]
        hashBits = mfc.hash(oriImg.shape[1], oriImg.shape[0], imgBlock)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])
        bitmap = ifc.xor(markBlock, hashBits)
        block = ifc.insert2LSB(imgBlock, bitmap)
        blocks.append(block)
    dst = ifc.assembleBlocks(blocks, (oriImg.shape[0], oriImg.shape[1]))
    if oriImg.ndim == 3:#colored
        dst = ifc.merge(dst, oriImg)
    return dst