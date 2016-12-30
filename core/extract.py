from utils import imageFunc as ifc
from utils import mathFunc as mfc
from preprocess import preprocess
import copy

def extract(img):
    testImg = copy.deepcopy(img)
    if testImg.ndim == 3:#colored
        img = ifc.getGChn(testImg)
    imgBlocks = ifc.splitImg(img)
    zeroedBlocks = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    extractedLSBs = map(lambda b: ifc.extractLSB(b), imgBlocks)
    blocks = list()
    for i in xrange(len(imgBlocks)):
        imgBlock = imgBlocks[i]
        zeroedBlock = zeroedBlocks[i]
        extractedLSB = extractedLSBs[i]
        hashBits = mfc.hash(testImg.shape[1], testImg.shape[0], zeroedBlock)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])#64
        dstBlock = ifc.xor(extractedLSB, hashBits)
        blocks.append(dstBlock)
    dst = ifc.assembleBlocks(blocks, (testImg.shape[0], testImg.shape[1]))
    dst *= 255
    return dst