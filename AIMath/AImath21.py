# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#ベクトルの線形変換の実装
a = np.array([2,3]) #変換前のベクトル
A = np.array([[2,-1],
	     [2,-2]])
b = np.dot(A,a) #線形変換

print("変換前のベクトル(a):",a)
print("変換後のベクトル(b):",b)  

def arrow(start,size,color):
	plt.quiver(start[0],start[1],size[0],size[1],angles="xy",scale_units="xy",scale=1,color=color)

s = np.array([0,0]) #原点
arrow(s,a,color="black")
arrow(s,b,color="blue")
#グラフ表示
plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel("x",size=15)
plt.ylabel("y",size=15)
plt.grid()
plt.axes().set_aspect("equal") #縦横比を同じに
plt.show()
