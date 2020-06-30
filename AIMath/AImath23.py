# -*- coding: utf-8 -*-
import numpy as np

#コサイン類似度計算の実装
def cos_sim(vec_1,vec_2):
	return np.dot(vec_1,vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))

a = np.array([2,2,2,2])
b = np.array([1,1,1,1]) #aと同じ向き
c = np.array([-1,-1,-1,-1]) #aと反対向き

print(cos_sim(a,b)) #aとbのコサイン類似度
print(cos_sim(a,c)) #aとcのコサイン類似度