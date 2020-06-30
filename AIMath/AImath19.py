# -*- coding: utf-8 -*-
import numpy as np

#行列式の実装
a = np.array([[1,2],
	    [3,4]]) 
print(np.linalg.det(a)) #行列式が0にならない場合

b = np.array([[1,2],
	    [0,0]]) 
print(np.linalg.det(b)) #行列式が0になる場合