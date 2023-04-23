# -*- coding: utf-8 -*-
from 输出电压计算 import voltageout
import numpy as np
from 输出电压计算 import sol


def run(i, Panode, Pcathode, Troom, Tinitial, t):
    import time
    t1 = time.time()
    v = np.array([])
    T = np.array([])
    a = len(i)
    b = len(t)
    if a < b:
        m = np.ones_like(t)
        m[:a] = i
        m[a:] = i[a - 1]
        i = m

    for m in range(len(t)-1):
        tx = [t[m], t[m+1]]
        x = i[m]
        y = sol(x, Panode, Pcathode, Troom, Tinitial, tx)  # Y返回的是温度和电压
        Tinitial = y[0]
        v = np.hstack((v,y[1]))  # 记录电压
        T = np.hstack((T,y[0]))  # 记录温度
    t2 = time.time()
    print(f"求解 用时{t2 - t1}")
    import matplotlib.pyplot as plt
    plt.plot(t[1:],v)

    plt.show()
    plt.plot(t[1:],T)
    plt.show()
