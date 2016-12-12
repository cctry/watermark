# -*- coding: utf-8 -*
import md5
import numpy
def decPrime(num):
    res = set()
    for i in xrange(2,num+1):
        while num!=i:
            if num%i == 0:
                res.add(i)
                num = num/i
            else:
                break
    res.add(num)
    return list(res)

def getBlockSize(hli, wli, MAX):#output [height, width]
    if hli[len(hli) - 1] >= wli[len(wli) - 1]:
        bli = hli
        sli = wli
        flag = 1
    else:
        bli = wli
        sli = hli
        flag = 2
    size = list()
    for i in xrange(1, len(sli)):
        for j in xrange(1, len(bli)):
            if (sli[-i] * bli[-j]) <= MAX:
                if flag == 1:
                    windex = len(wli) - i
                    hindex = len(hli) - j 
                if flag == 2:
                    windex = len(wli) - j 
                    hindex = len(hli) - i 
                break
            else:
                continue
    size.append(hli[hindex])
    size.append(wli[windex])    
    return size                

def hash(M, N, block):#return bit array
    m = md5.new()
    m.update(str(M))
    m.update(str(N))
    m.update(block)
    temp = m.digest()
    biStrTemp = list()
    for char in temp:
        deTemp = ord(char)
        binTemp = bin(deTemp)
        binTemp = binTemp[2:]
        if len(binTemp) < 8:
            pre = '0' * (8-len(binTemp))
            binTemp = pre + binTemp
        biStrTemp.append(binTemp)
    nullStr = ''
    resTemp = nullStr.join(biStrTemp)
    bitArray = list()
    for i in xrange(len(resTemp)):
        res.append(resTemp[i])
    return bitArray

def cutHash(hash, len):
    hash = hash[0:len]
    return hash

def reshape(bitarray, size):
    bitBlock = numpy.array(bitarray).reshape(size[0], size[1])
    return bitBlock
