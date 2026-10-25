import numpy as np

def extract_subarray(arr: list, row_start: int, row_stop: int, col_start: int, col_stop: int) -> np.ndarray:

    arr = np.array(arr, dtype = np.float64)
    b = arr[row_start:row_stop, col_start:col_stop]

    return b
    
