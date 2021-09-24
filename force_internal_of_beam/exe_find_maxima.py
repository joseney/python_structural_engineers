import numpy as np


def find_maxima(a):
    maxima = []
    index = []
    n = len(a)
    for i in range(n):
        if a[0] > a[1]:
            maxima.append(a[0])
            index.append(i)
        elif i == n - 1:
            if a[-1] > a[-2]:
                maxima.append(a[-1])
                index.append(i)
        else:
            if a[i] >= a[i - 1] and a[i] > a[i + 1]:
                maxima.append(a[i])
                index.append(i)


M_pos_max, index_pos_M = find_maxima(M_pos)
M_neg_max, index_neg_M = find_maxima(abs(M_neg))
M_pos_max = np.array(M_pos_max)
M_neg_max = np.array(M_neg_max)

V_pos_max, index_pos_V = find_maxima(V_pos)
V_neg_max, index_neg_V = find_maxima(abs(V_neg))
V_pos_max = np.array(V_pos_max)
V_neg_max = -np.array(V_neg_max)