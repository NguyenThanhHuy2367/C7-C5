"""
Created on Sun Sep 29 20:11:51 2024

@author: NGUYEN THANH HUY
"""

def tong(*args, **kwargs):
    return sum(args)
def tich(*args, **kwargs ):
    b = 1
    for i in args:
        b *= i
    return  b
#if __name__=="__main__":
ds = (1, 2, 3, 4, 5)
print("tổng:", tong(*ds))
print("Tích", tich(*ds))