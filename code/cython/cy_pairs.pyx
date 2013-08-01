from libc.math cimport sqrt
import numpy as np


cpdef dist(double[:, ::1] x):
    cdef int n = x.shape[0]
    cdef int m = x.shape[1]
    cdef double[:, ::1] ret = np.empty((n, n))
    cdef double d, tmp
    cdef int i, j, k
    for i in range(n):
        for j in range(n):
            d = 0.0
            for k in range(m):
                tmp = x[i, k] - x[j, k]
                d += tmp * tmp
            ret[i, j] = sqrt(d)
    return ret
