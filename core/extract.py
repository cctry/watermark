from utils import imageFunc as ifc
from utils import mathFunc as mfc
import copy

def extract(img):
    oriImg = copy.deepcopy(img)
    if oriImg.ndim == 3:
        img = ifc.getGChn(img)
    imgBlocks = ifc.splitImg(img)
    LSBs = map(lambda b: ifc.extractLSB(b), imgBlocks)
    zeroedLSBs = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    blocks = list()
    for i in xrange(len(imgBlocks)):
        imgBlock = zeroedLSBs[i]
        LSB = LSBs[i]
        hashBits = mfc.hash(imgBlock.shape[1], imgBlock.shape[0], imgBlock)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0] * imgBlock.shape[1])
        dstBlock = ifc.xor(LSB, hashBits)
        blocks.append(dstBlock)
    dst = ifc.assembleBlocks(blocks, (oriImg.shape[0], oriImg.shape[1]))
    return dst*255