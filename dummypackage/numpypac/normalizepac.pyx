import numpy as np
cimport numpy as np


# np.import_array() -> for cython 3

DTYPE = np.int # datatype for array
ctypedef np.int_t DTYPE_t # corresponding compile-time to DTYPE_t


def normalize(np.ndarray[DTYPE_t, ndim=1] arr):
    cdef int n = arr.shape[0]
    cdef int i
    cdef float norm

    norm = 0    
    for i in range(n):
        norm += arr[i] ** 2
    
    return norm ** (0.5)