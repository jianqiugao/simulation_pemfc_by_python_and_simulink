import math
from 有效压力 import valid_pressure


def ecell(i, T, panode, pcathode):
    # 单电池电压
    def EoCELL():  # 参考电位
        return 1.229

    po2, ph2 = valid_pressure(i, T, panode, pcathode)
    # print(po2, ph2 )

    return math.log(math.sqrt(po2) * ph2, math.e) * 4.3085e-5 * T \
           + EoCELL() - (T - 298.15) * 0.85e-3, \
           237.2e3 - ((T - 298.15) * 0.163) + (8.31 * (math.log(math.sqrt(po2) * ph2, math.e)) * T)


if __name__ == "__main__":
    import numpy as np
    a = ecell(1, 292, 1, 1)
    print(a)
    i = np.linspace(0,1,10)

    b = []
    for x in i:
        y = ecell(x, 303, 1, 1)
        print(y)
        b.append(y[0])
    import matplotlib.pyplot as plt
    plt.plot(i,b)
    plt.show()
