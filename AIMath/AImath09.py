# -*- coding: utf-8 -*-
import numpy as np

#乱数を実装
r_int = np.random.randint(5) + 1 #0-4までの乱数に1加える
r_dec = np.random.rand() #0-1までの間の小数をランダムに生成
print(r_int)
print(r_dec)