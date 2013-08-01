from math import sqrt
import numpy as np


def dist(x):
    n = x.shape[0]
    m = x.shape[1]
    ret = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            d = 0.0
            for k in range(m):
                tmp = x[i, k] - x[j, k]
                d += tmp * tmp
            ret[i, j] = sqrt(d)
    return ret
