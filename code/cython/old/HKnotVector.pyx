import numpy as np
cimport numpy as np
cimport cpp_HKnotVector
from libcpp.vector cimport vector as cpp_vector
from libc.stdlib cimport free

np.import_array()

cdef class HKnotVector:
    def __cinit__(self, *args, **kwargs):
        self._inst = NULL

    def construct_1(self):
        self._inst = new cpp_HKnotVector.HKnotVector()

    def construct_2(self, degree, knots):
        cdef:
            double * knots_data
            cpp_vector[double] cpp_knots
            int i

        cdef int knots_size = len(knots)
        if isinstance(knots, np.ndarray):
            knots_data = <double *> np.PyArray_DATA(<np.ndarray> knots)
            cpp_knots = cpp_vector[double](<size_t> knots_size)
            for i in range(knots_size):
                cpp_knots[i] = knots_data[i]
        else:
            cpp_knots = cpp_vector[double](knots_size)
            for i in range(knots_size):
                cpp_knots[i] = knots[i]
        self._inst = new cpp_HKnotVector.HKnotVector(<unsigned int> degree, cpp_knots)

    def __init__(self, *args):
        if len(args) > 0:
            self.construct_2(*args)
        else:
            self.construct_1(*args)

    def __dealloc__(self):
        free(self._inst)

    def degree(self):
        cdef unsigned int deg
        deg = (<cpp_HKnotVector.HKnotVector *> self._inst).degree()
        return int(deg)

    def isEven(self):
        cdef bint even
        even = (<cpp_HKnotVector.HKnotVector *> self._inst).isEven()
        return bool(even)

    def isOdd(self):
        cdef bint odd
        odd = (<cpp_HKnotVector.HKnotVector *> self._inst).isOdd()
        return bool(odd)
