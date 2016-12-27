# -*- coding: utf-8 -*
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import mathFunc as mfc

class encryptor:
    #attributes
    random_generator = Random.new().read
    #methods
    def generateKey(self, length):#length is as long as the block size times 8
        rsa = RSA.generate(length, self.random_generator)#make sure the length after encrypt is qulify
        private_pem = rsa.exportKey()#
        with open('private.pem', 'w') as f:
            f.write(private_pem)
        public_pem = rsa.publickey().exportKey()
        with open('public.pem', 'w') as f:
            f.write(public_pem)

    def loadKey(self, filename):
        with open(filename) as f:
            key = f.read()
        return key
        
    def encrypt(self, key, img):
        msg = self.preprocess(img)
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_msg = cipher.encrypt(img)
        return cipher_msg

    def decrypt(self, key, msg):
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(msg, self.random_generator)
        return text

    def preprocess(self, img):#preprocess the image: convert matrix to str
        lst = img.tolist()
        temp = list()
        for ele in lst:
            temp += ele
        bitarray = map(lambda a: int(a), temp)#from left to right, from up to down
        res = mfc.bit2str(bitarray)#convert list to str
        return res
