import numpy as np

def mahalanobis_distance(x, mean, cov):
    x, mean, covv = np.array(x), np.array(mean), np.array(cov)
    return ((x - mean).T @ np.linalg.inv(cov) @ (x - mean))**0.5
    