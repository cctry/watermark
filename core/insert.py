from utils import imageFunc as ifc
from utils import mathFunc as mfc
from utils import rsa as RSA

def insert(img, mark, key = None):#TODO key
    oriImg, img, mark = preprocess(img, mark)
    imgBlocks = ifc.splitImg(img)
    markBlocks = ifc.splitImg(mark)
    imgBlocks = map(lambda b: ifc.zeroLSB(b))
    rsa = RSA.rsa()
    #TODO about key
    #pub = public key
    #pri = private key
    for i in xrange(len(imgBlocks)):
        imgBlock = imgBlocks[i]
        markBlock = markBlocks[i]
        hashBits = mfc.hash(oriImg.shape[1], oriImg.shape[0], imgBlock)
        hashBits = mfc.cutHash(hashBits, imgBlock.shape[0]*imgBlock.shape[1])
        bitmap = ifc.xor(markBlock, hashBits)
        encrypted_block = rsa.encrypt(pub, bitmap)
        #TODO insert to LSB
