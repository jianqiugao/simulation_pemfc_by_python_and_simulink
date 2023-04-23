from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


def func(t, z):
    y = z[0]
    x = z[1]
    dydt = 1000 * (1 - x ** 2)*y - x
    dxdt = y
    return [dydt,dxdt]


f = solve_ivp(func, [0,6000], [0, 2], method ='Radau')

plt.plot(f.t,f.y[1,:])
plt.show()
