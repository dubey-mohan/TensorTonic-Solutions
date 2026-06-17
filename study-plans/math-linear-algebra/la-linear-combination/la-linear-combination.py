import numpy as np

def linear_combination(vectors, coefficients):

    v = np.array(vectors)
    c = np.array(coefficients)

    return np.dot(v.T, c)

    
        
        