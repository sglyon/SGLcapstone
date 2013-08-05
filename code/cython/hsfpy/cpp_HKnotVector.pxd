from libcpp.vector cimport vector as cpp_vector

cdef extern from "HKnotVector.h" namespace "hsf":

    cdef cppclass HKnotVector:
        # constructors
        HKnotVector()
        HKnotVector(unsigned int, const cpp_vector[double] &)

        # methods
        unsigned int degree()
        bint isEven()
        bint isOdd()
