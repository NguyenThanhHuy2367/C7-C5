# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:10:47 2024

@author: NGUYEN THANH HUY
"""

n = int(input("Nhập một số nguyên dương n: "))
giai_thua = 1
for i in range(1, n + 1 ):
    giai_thua = giai_thua * i
print("Giai thua bang: ", giai_thua)