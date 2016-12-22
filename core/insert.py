from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA
from preprocess import preprocess

def insert(img, mark, key):#TODO key
    oriImg, img, mark = preprocess(img, mark)#flag
    imgBlocks = ifc.splitImg(img)
    markBlocks = ifc.splitImg(mark)
    imgBlocks = map(lambda b: ifc.zeroLSB(b))
    rsa = RSA.rsa()
    blocks = list()
    for i in xrange(len(imgBlocks)):
        imgBlock = imgBlocks[i]
        markBlock = markBlocks[i]
        hashBits = mfc.hash(oriImg.shape[1], oriImg.shape[0], imgBlock)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])
        bitmap = ifc.xor(markBlock, hashBits)
        encrypted_block = rsa.encrypt(key, bitmap)
        block = ifc.insert2LSB(imgBlock, encrypted_block)
        blocks.append(block)
    dst = ifc.assembleBlocks(blocks, (oriImg.shape[0], oriImg.shape[1]))
    res = ifc.merge(dst, oriImg)
    return res