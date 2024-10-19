# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:35:38 2024

@author: NGUYEN THANH HUY
"""
import random
def tao_seqA():
    n= random.randint(30,80)
    seqA = []
    for i in range(n+1):
        if random.randint(0,1) == 0 :
            seqA.append(round(random.uniform(-79,39),2))
        else :
            seqA.append(random.randint(-79,39))
    return seqA 

    
#2
def ktra(seqA):
    return [type(i).__name__ for i in seqA ]

#3 
def thongke(seqA):
    return len(seqA)

#4
def sapxep_seqB(seqA):
    return sorted(seqA)

#5
def trungbinh(seqA):
    return round(sum(seqA)/len(seqA),2)


#6  ([1234] = trung bình giữa 2 phần thử nằm giữa, khi n chẵn )

def trungbinh_seqB(seqB):
    n = len(seqB)
    if n%2==0:
        return (seqB[n//2 - 1 ] + seqB[n//2]) / 2
    else:
        return seqB[n//2]
    
#7
def khoangcach(seq):
    return max(seq)-min(seq)

#8
def sosanh(seqA,seqB):
    return trungbinh(seqA),trungbinh_seqB(seqB), trungbinh(seqA)==trungbinh_seqB(seqB)


if __name__=="__main__":
    seqA=tao_seqA()
    print(seqA)
    print("==2==")
    print(ktra(seqA))
    print("==3==")
    print(thongke(seqA))
    print("==4==")
    seqB= sapxep_seqB(seqA)
    print(sapxep_seqB(seqA))
    print("==5==")
    print(trungbinh(seqA))
    print("==6==")
    print(trungbinh_seqB(seqB)) 
    print("==7==")
    print(khoangcach(seqA))
    print(khoangcach(seqB))
    print("==8==")
    sosanhAB = sosanh(seqA,seqB)
    print(sosanhAB)