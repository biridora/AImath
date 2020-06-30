# -*- coding: utf-8 -*-
import numpy as np

#固有値と固有ベクトル計算の実装
a = np.array([[-2,4],
	    [1,3]]) 

ev = np.linalg.eig(a) #固有値と固有ベクトルを同時に求める
print(ev[0]) #固有値
print(ev[1]) #固有ベクトル