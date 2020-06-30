# -*- coding: utf-8 -*-
import numpy as np

#ノルムの実装
a = np.array([1,1,-1,1]) 

print("----L2ノルム----")
print(np.linalg.norm(a)) #L2ノルム(デフォルト)
print("---L1ノルム----")
print(np.linalg.norm(a,1)) #L1ノルム