from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA
from preprocess import preprocess

def extract(img,key):
    testimg,img = ifc.getGChn(testimg)#flag
    imgBlocks = ifc.splitImg(img)
    imgBlocks1 = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    imgBlocks2 = ifc.extractLSB(imgBlocks)
    imgBlocks2 = RSA.decrypt(key,imgBlocks2)
    blocks = list()
    for i in xrange(len(imgBlocks1)):
        imgBlock = imgBlocks1[i]
        hashBits = mfc.hash(testImg.shape[1], testImg.shape[0], imgBlock1)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])
        bitmap = ifc.xor(imgBlocks2, hashBits)
        decrypted_block = RSA.decrypt(key,msg)
        block = ifc.insert2LSB(imgBlock, decrypted_block)
        blocks.append(block)
    dst = ifc.assembleBlocks(blocks, (testImg.shape[0], testImg.shape[1]))
    res = ifc.merge(dst,testImg)
    return res