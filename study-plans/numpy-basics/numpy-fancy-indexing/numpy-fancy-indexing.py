import numpy as np

def select_by_index(arr: list, indices: list, axis: int) -> np.ndarray:
    arr = np.array(arr, np.float64)
    return np.take(arr, indices, axis = axis)
    
