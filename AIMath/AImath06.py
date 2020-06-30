# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot  as plt

#y=sinx,y=cosxを実装

def my_sin(x):
	return np.sin(x) # sin(x)

def my_cos(x):
	return np.cos(x) # cos(x)

x = np.linspace(-np.pi,np.pi) #-πからπ(ラジアン)までの範囲
y_sin = my_sin(x)
y_cos = my_cos(x)
plt.plot(x,y_sin,label="sin")
plt.plot(x,y_cos,label="cos")
plt.legend()
plt.xlabel("x",size=15)
plt.ylabel("y",size=15)
plt.grid()
plt.show()