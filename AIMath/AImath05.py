# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot  as plt

#3次の多項式y=5x^3+2x^2+x+5を実装
def myfunction(x):
	return 5*x**3 + 2*x**2 + x + 5
x = np.linspace(-2,2)
y = myfunction(x) #y=f(x)
plt.plot(x,y)
plt.xlabel("x",size=15)
plt.ylabel("y",size=15)
plt.grid()
plt.show()