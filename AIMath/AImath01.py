# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot  as plt

#定数と変数を扱った実装

b  = 5 #b:定数
x = np.linspace(-2,2) #x:変数　 
y = b * x # y:変数
plt.plot(x,y)
plt.xlabel("x",size=15)
plt.ylabel("y",size=15)
plt.grid()
plt.show()