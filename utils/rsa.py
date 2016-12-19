# -*- coding: utf-8 -*
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import mathFunc as mfc
#global var
random_generator = Random.new().read
#functions
def generateKey():
    global random_generator
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa.exportKey()#
    with open('private.pem', 'w') as f:
        f.write(private_pem)
    public_pem = rsa.publickey().exportKey()
    with open('public.pem', 'w') as f:
        f.write(public_pem)

def loadKey(filename):
    with open(filename) as f:
        key = f.read()
    return key
    
def encrypt(key, msg):
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_msg = base64.b64encode(cipher.encrypt(msg))
    return msg

def decrypt(key, msg):
    global random_generator
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(msg), random_generator)

def preprocess(img):#preprocess the image: convert matrix to str
    lst = img.tolist()
    temp = list()
    for ele in lst:
        temp += ele
    bitarray = map(lambda a: int(a), temp)#from left to right, from up to down
    res = mfc.bit2str(bitarray)#convert list to str
    return res
