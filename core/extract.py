from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA
from preprocess import preprocess

def extract(img,key):
    testImg = copy.deepcopy(img)
    if testImg.ndim == 3:#colored
        img = ifc.getGChn(testImg)
    imgBlocks = ifc.splitImg(img)
    zeroedBlocks = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    extractedBlocks = map(lambda b: ifc.extractLSB(b), imgBlocks)
    blocks = list()
    for i in xrange(len(imgBlocks)):
        imgBlock = imgBlocks[i]
        zeroedBlock = zeroedBlocks[i]
        extractedBlock = extractedBlocks[i]
        hashBits = mfc.hash(testImg.shape[1], testImg.shape[0], zeroedBlock)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])
        bitmap = ifc.xor(extractedBlock, hashBits)
        dst = ifc.assembleBlocks(bitmap, (testImg.shape[0], testImg.shape[1]))
    return dst