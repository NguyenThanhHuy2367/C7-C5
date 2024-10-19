# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:13:35 2024

@author: NGUYEN THANH HUY
"""

while True:
    a = int(input("Nhap gia tri tu [-99,99]: "))
    if -99 <= a <= 99:
        print("Hop le", a)
        break
    else:
        print("Khong hop le")