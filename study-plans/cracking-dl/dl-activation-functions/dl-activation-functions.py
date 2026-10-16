import numpy as np

def activation_functions(x: float, activation: str) -> list:

    if activation == 'relu':
        func = x if x > 0 else 0
        diff = 1 if x > 0 else 0
    
    elif activation == 'leaky_relu':
        func = x if x > 0 else 0.01*x
        diff = 1 if x > 0 else 0.01
        
    elif activation == 'sigmoid':
        func =  1 / (1 + np.exp(-x))
        diff =  func * (1 - func)
        
    elif activation == 'tanh':
        func = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
        diff = 1 - func**2

    elif activation == 'gelu':
        a = np.sqrt(2 / np.pi)
        u = a * (x + 0.044715 * x**3)
        t = np.tanh(u)
        func = 0.5 * x * (1 + t)
        du = a * (1 + 3 * 0.044715 * x**2)
        diff = 0.5 * (1 + t) + 0.5 * x * (1 - t**2) * du

    elif activation == 'swish':
        sigmoid = 1 / (1 + np.exp(-x))
        func = x * sigmoid
        diff = sigmoid + x * sigmoid * (1 - sigmoid)

    else:
        raise ValueError("Function out of list")


    return [func, diff]


    
