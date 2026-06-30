import numpy as np

def cholesky_decompose(A):
    A = np.array(A)
    r = len(A)
    c = len(A[0])
    L = np.zeros((r, c))

    if not np.allclose(A, A.T):
        return None

    for i in range(c):
        for j in range(i + 1):
            if i == j:
                L_jk = 0
                for k in range(j):
                    L_jk += L[j, k]**2
                check = A[j, j] - L_jk
                if check <= 0:
                    return None
                else:
                    L[j, j] = (check)**0.5
            else:
                L_ik = 0
                for k in range(j):
                    L_ik += L[i, k]*L[j, k]
                L[i, j] = (A[i, j] - L_ik) / L[j, j]
    
    return L
                    
                    

    
    