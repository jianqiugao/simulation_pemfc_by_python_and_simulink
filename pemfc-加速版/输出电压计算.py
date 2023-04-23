# -*- coding: utf-8 -*-
from 热量计算 import heattotal
from scipy.integrate import solve_ivp
import numpy as np
from 能斯特电压 import ecell
from 单电池电压损失 import conc, act1, act2, ohmic


def voltageout(I, T, Panode, Pcathode, Troom, Tinitial, tx):
    eps = 0.000001
    ecel = (ecell(I, T, Panode, Pcathode))[0]
    conc_ = conc(I, T)
    act1_ = act1(T)
    act2_ = act2(I, T)
    ohmic_ = ohmic(I, T)
    v0 = 0
    v1 = conc_ / (eps + I) + (act2_ / (eps + I))
    t1 = tx[0]
    t2 = tx[1]

    def fun(t, x):
        vc = x[1]
        v = (ecel - vc - act1_ - ohmic_) * 48  # 通过输入计算电压
        dg = (ecell(I, T, Panode, Pcathode))[1]
        heat = heattotal(I, v, Troom, T, dg)
        dydt = (I + 0.001 - vc / v1) / 4  # 浓差电压损失导数
        return [heat, dydt]
    T = solve_ivp(fun, (t1, t2), [Tinitial, v0], method='DOP853')

    v = T.y[1].reshape(-1)
    t = T.t
    v = (ecel - v - act1_ - ohmic_) * 48

    return T, v, t


def sol(I, Panode, Pcathode, Troom, Tinitial, tx):

    T = 305 # 温度已经设置为中间参数了，这个值越合理则wegstein迭代的步数越少，当然目前最多也就5步，远远小于设定的30步

    # 采用wegstein方法去迭代真的快
    def func(T):
        t, v, ti= voltageout(I, T, Panode, Pcathode, Troom, Tinitial, tx)  # 还是这个函数调用一次太费时间了
        t = t.y[0].reshape(-1)  # 返回最后一个时间点的温度
        v = v.reshape(-1)
        return t, v , ti

    def wegstein(y, num):  # 一种迭代算法
        eps = np.array(0.0001)  # 一个小数，免得除0的情况发生，由于是
        for i in range(num):
            inte = func(y)
            gk_1 = inte[0][-1]   # 返回的是温度
            intv = inte[1][-1]  # 把这个值取出来，最后返回，中间不会使用
            gk_ = func(gk_1)[0]
            gk = gk_[-1]
            xk_1 = y
            x_k = gk_1
            s = (gk - gk_1) / (x_k - xk_1 + eps)
            q = s / (s - 1)
            y = (q * x_k + (1 - q) * gk)  # 计算出来的温度
            if abs(x_k - xk_1) < eps:
                # print(f"提前结束循环{i + 1}次")
                break

        return y, intv

    return wegstein(T, 30)


if __name__ == "__main__":
    I = np.array(20)
    T = np.array(385)
    Panode = np.array(1)
    Pcathode = np.array(1)
    Troom = np.array(273 + 15)
    Tinitial = np.array(303.15)
    tx = np.array([0, 10])

    import time
    t1 = time.time()
    i = np.linspace(0.5, 28.5, 30)
    b = []  # 温度
    for x in i:
        y = sol(x, Panode, Pcathode, Troom, Tinitial, tx)
        b.append(y[0])
    p = b * i
    t2 = time.time()
    print(t2 - t1)
    import matplotlib.pyplot as plt
    plt.plot(i, b)
    # plt.plot(i, p)
    plt.show()
