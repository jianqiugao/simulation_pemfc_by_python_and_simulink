import pandas as pd
from 画图模块 import run
import numpy as np

i = pd.read_csv("负载电流.csv").values

# i = np.linspace(10, 20, 20)  # 求解的输入i
# t = np.linspace(0, 20+1000, len(i)+100)  # 计算的时间区间

t = i[:3000, 0]
i = i[:3000, 1]
#
Panode = 1.5  # 阴极压力bar
Pcathode = 1  # 阳极压力bar
Troom = 307.7  # 环境温度
Tinitial = 307.7  # 初始温度

run(i, Panode, Pcathode, Troom, Tinitial,t)


