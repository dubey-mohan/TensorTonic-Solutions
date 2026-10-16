import numpy as np

def dropout(X: list, mask: list, drop_prob: float, mode: str) -> list:
    X = np.array(X)
    M = np.array(mask)
    dropout = 1 - drop_prob

    if mode == 'train':
        return (X * M) / dropout
    else:
        return X
        

    
    
