import numpy as np

def perceptron(X: list, y: list, lr: float = 0.1, epochs: int = 100) -> tuple:
    X = np.array(X, dtype = float)
    y = np.array(y)
    w = np.zeros(X.shape[1])
    b = 0.0

    for _ in range(epochs):
        for x, y_i in zip(X, y):
            z = w @ x + b
            
            y_pred = 1 if z >= 0 else 0
            err = y_i - y_pred

            if y_pred != y_i:
                w += lr*err*x
                b += lr*err

          

    return w, b
    
