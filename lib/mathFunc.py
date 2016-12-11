# -*- coding: utf-8 -*
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
    res = list()
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
    res.append(hli[hindex])
    res.append(wli[windex])    
    return res                
