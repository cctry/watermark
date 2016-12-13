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

def allFct(num):#Just for fun, I use a special algorithm
    decPri = decPrime(num)
    res = set()
    res.add(num)
    exp = list[]
    n = 0
    for ele in decPri:
        while num%ele == 0:
            num = num/ele
            n++
        exp.append(n)
        n = 0
    #use decorator here
    
    return list(res)

def getBlockSize(shape, MAX):#output [height, width] TODO
    size = list()
    hList = allFct(shape[0])
    wList = allFct(shape[1])
    height = shape[0]
    width = shape[1]
    dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))#??? WTF!
    combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
    bigmuls = lambda xs,ys: filter(lambda (x,y):x*y <= MAX, combine(xs,ys))# I hate FP!!
    temp = bigmuls(hList, wList)

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
