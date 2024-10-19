# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:20:47 2024

@author: NGUYEN THANH HUY
"""

def kiemtragiatri():
    n=int(input("Kiểm tra giá trị nhập n ="))

    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
        if -89  <= n <= 90:
            return n 
        print("Không hợp lệ")
print(kiemtragiatri(4))