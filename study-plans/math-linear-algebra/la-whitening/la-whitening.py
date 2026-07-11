import numpy as np

def whiten(X):

    X = np.array(X)
    Xcent = X - np.mean(X, axis = 0)
    Xcov = np.cov(Xcent, rowvar = False)
    eVal, eVec = np.linalg.eigh(Xcov)
    inv_sqrt = np.zeros_like(eVal)
    mask = eVal > 1e-12
    inv_sqrt[mask] = 1 / np.sqrt(eVal[mask])
    D_inv = np.diag(inv_sqrt)
    Xw = Xcent @ eVec @ D_inv
    return Xw
    
    
    