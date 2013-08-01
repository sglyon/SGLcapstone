from hbspy cimport cpp_HKnotVector

cdef class HKnotVector:
    cdef void * _inst
    cdef public bint _free_inst
