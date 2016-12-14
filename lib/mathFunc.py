# -*- coding: utf-8 -*
import md5
import numpy
import math

def allFct(num):
    res = list()
    for i in xrange(2,num+1):
        if num%i == 0:
            res.append(i)
    return res

def getBlockSize(shape, MAX):#output [height, width] TODO
    hList = allFct(shape[0])
    wList = allFct(shape[1])
    height = shape[0]
    width = shape[1]
    dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
    combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
    bigmuls = lambda xs,ys: filter(lambda (x,y):x*y <= MAX, combine(xs,ys))# I hate FP!!
    temp = bigmuls(hList, wList)
    std = 0
    for ele in temp:
        if (ele[0]*ele[1]) > std:
            if math.fabs(ele[0] - ele[1]) <= 0.5*max(ele):
                size = ele
                std = ele[0]*ele[1]
            else:
                continue
        elif (ele[0]*ele[1]) == std:
            if math.fabs(ele[0] - ele[1]) > math.fabs(size[0] - size[1]):
                size = ele
            else:
                continue
        else:
            continue
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
