import numpy as np
from scipy.integrate import solve_ivp


def heatcac(I, T, Troom):
    """显热，潜热"""
    T1 = I * 1 / (2.0 * 96487.0) * 28.68 * (2 * Troom - T)
    T2 = I * 1 / (4.0 * 96487.0) * 29.39 * (2 * Troom - T)
    T3 = I * 1 / (2.0 * 96487.0) * 75.4 * (T - Troom)
    T4 = I*1.0 / (2.0 * 96487.0) * 40644
    T5 = (T1 + T2 + T4 + T3)*48
    return T5


def heatloss(T, Troom):
    heatl = 24 * 3.2e-2 * 37.5 * (T - Troom)
    return heatl


def hreaction(I, deltaG):
    HR = I * 1 / (2.0 * 96487.0) * deltaG * 48
    return HR


def hele(I, V):
    HE = I * V
    return HE


def heattotal(I, V, Troom, T,deltaG):
    HEAT = (-hele(I, V) - heatloss(T, Troom) - heatcac(I, T, Troom) + hreaction(I, deltaG))*1/(2.2e4)
    return HEAT


