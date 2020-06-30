# -*- coding: utf-8 -*-
import numpy as np

#数学関数「y=5x+4」をプログラムの関数として実装
def myfunction(x):
	return 5*x + 4 # 一次関数5x +4

x=2
y = myfunction(x) # y= f(x)
print(y)