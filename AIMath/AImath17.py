# -*- coding: utf-8 -*-
import numpy as np

#行列積の実装
a = np.array([[0,1,2],
	    [1,2,3]]) 
b = np.array([[2,1],
	      [2,1],
	      [2,1]]) 

print(np.dot(a,b))