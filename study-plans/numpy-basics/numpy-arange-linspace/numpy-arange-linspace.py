import numpy as np

def create_sequence(start: float, stop: float, param: float, kind: str) -> np.ndarray:

    if kind == 'arange':
        return np.arange(start, stop, param, dtype = np.float64)
    else:
        return np.linspace(start, stop, param)

   
