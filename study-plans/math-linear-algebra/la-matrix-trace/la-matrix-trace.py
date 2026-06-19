import numpy as np

def matrix_trace(A):

    n = len(A)
    r = 0
    for i in range(n):
        r += A[i][i]
    return r