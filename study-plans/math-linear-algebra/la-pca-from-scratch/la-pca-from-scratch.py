import numpy as np

def pca_project(X, n_components):

    X = np.array(X, dtype = float)

    rows = len(X)
    cols = len(X[0])

    # center the given data
    for c in range(cols):
        X[:, c] = X[:, c] - np.mean(X[:, c])

    cov = (X.T @ X) / (rows - 1)
    eigen_val, eigen_vec = np.linalg.eigh(cov)
   
    idx = np.argsort(eigen_val)[::-1]
    n_comp = eigen_vec[:, idx]

    k_comp = n_comp[:,:n_components]

    proj_X =X @ k_comp

    return proj_X
    
        
    