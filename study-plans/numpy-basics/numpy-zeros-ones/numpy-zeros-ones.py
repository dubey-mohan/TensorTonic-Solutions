import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:

    if kind == "zeros":
        return np.zeros(shape)
    else:
        return np.ones(shape)
    
