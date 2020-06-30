# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot  as plt

#数式y=√xを実装
def myfunction(x):
	return np.sqrt(x) # xの正の平方根
x = np.linspace(0,9)
y = myfunction(x) #y=f(x)
plt.plot(x,y)
plt.xlabel("x",size=15)
plt.ylabel("y",size=15)
plt.grid()
plt.show()