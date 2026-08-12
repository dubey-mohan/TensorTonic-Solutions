import numpy as np

def activation_derivative(name, x):
    """
    Returns: list of floats (the derivative evaluated at each x)
    """
    o = []
    
    for val in x:
        if name == "sigmoid":
            sig = 1 / (1 + np.exp(-val))
            diff = sig*(1 - sig)
        elif name == "tanh":
            diff = 1 - np.power(np.tanh(val), 2)
        elif name == "relu":
            diff = 1 if val > 0 else 0
        else:
            sig = 1 / (1 + np.exp(-val))            
            diff = sig + val * sig * (1 - sig)
        
        o.append(diff)

    return o
            
