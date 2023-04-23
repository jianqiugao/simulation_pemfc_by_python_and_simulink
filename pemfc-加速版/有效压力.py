import math


def valid_pressure(I, T, panode, pcathode):
    """
    I
    T
    panode
    pcathode
    """

    def WATERPRESSURE(T):
        # 饱和水压力
        return (-40529.4522405347 + 401.94033912153 * T - 1.33430273535993 * (T ** 2) + 0.00148378443819808 * (
                T ** 3)) / 760
    # print(WATERPRESSURE(T))

    def water_x(C, T):
        # 水的摩尔分数
        return WATERPRESSURE(T) / panode

    def ph2(I, T, panode):
        # 定义氢气的有效分压
        return abs(1 / (math.exp(I * 5 * 1.653 / T ** 1.334) * water_x(panode, T)) - 1) * 0.5 * WATERPRESSURE(T)

    def pO2(I, T, pcathode):
        return abs(1 / (math.exp(I * 5 * 4.192 / T ** 1.334) * WATERPRESSURE(T) / pcathode) - 1) * WATERPRESSURE(T)

    return pO2(I, T, pcathode), ph2(I, T, panode)


if __name__ == "__main__":
    b = valid_pressure(10, 293.15, 1, 1)
    print(b)
