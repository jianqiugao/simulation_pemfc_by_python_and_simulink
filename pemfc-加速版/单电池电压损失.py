import math


def conc(I, T):
    # 浓差损失
    CONC = -2.6 * ((T * 4.3085e-5) * math.log((abs(1 - I / 25)) + 1.0e-100))
    CONC = max(CONC, 0)
    CONC = min(1, CONC)
    return CONC


def act1(T):
    ACT1 = (0.9514 * 1.0284 - 2.2e-3 * T) * 1.3
    return ACT1


def act2(I, T):
    ACT2 = T * ((1.87e-4 * math.log(I + 1)) * 0.40) * 1.3
    return ACT2


def ohmic(I, T):
    Ohmic = ((-0.0158 + (3.8e-5) * T) - (3.0e-5 * I)) * I * (-1.3)

    return Ohmic


if __name__ == "__main__":
    import numpy as np
    a = conc(25, 323.15)
    a = ohmic(25, 323.15)

    i = np.linspace(0.1, 25, 30)
    b = []
    for x in i:
        y = conc(x, 323.15)
        b.append(y)
    import matplotlib.pyplot as plt
    plt.plot(i, b)
    plt.show()
