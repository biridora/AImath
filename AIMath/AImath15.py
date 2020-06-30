# -*- coding: utf-8 -*-
import numpy as np

#内積の実装
a = np.array([1,2,3]) 
b = np.array([3,2,1]) 

print("---dot()関数による内積----")
print(np.dot(a,b))
print("---積の総和による内積----")
print(np.sum(a*b))