from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA
from preprocess import preprocess

def extract(img,key):
    if oriImg == 3：
        oriImg,img = ifc.getGChn(oriImg)#flag
    imgBlocks, size = ifc.splitImg(img)
    imgBlocks1 = map(lambda b: ifc.zeroLSB(b), imgBlocks)
    imgBlocks2 = ifc.extractLSB(imgBlocks)
    rsa = RSA.rsa()
    rsa.generateKey(size[0]*size[1])#len
    key = rsa.loadKey('public.pem')
    imgBlocks3 = RSA.decrypt(key,imgBlocks2)
    blocks = list()
    for i in xrange(len(imgBlocks1)):
        imgBlock = imgBlocks1[i]
        hashBits = mfc.hash(oriImg.shape[1], oriImg.shape[0], imgBlocks1)
        hashBits = mfc.cutHash(hashBits, imgBlocks3.shape[0]*imgBlocks3.shape[1])
        bitmap = ifc.xor(imgBlocks3, hashBits)
        decrypted_block = RSA.decrypt(key,bitmap)
        blocks.append(block)
    dst = ifc.assembleBlocks(blocks, (oriImg.shape[0], oriImg.shape[1]))
    return dst