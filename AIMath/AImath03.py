# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot  as plt

#数式y=x^aの実装
def myfunction(x):
	a = 6
	return x ** a # xのa乗
x = np.linspace(0,2)
y = myfunction(x)
plt.plot(x,y)
plt.xlabel("x",size=15)
plt.ylabel("y",size=15)
plt.grid()
plt.show()