import numpy as np

def filter_and_extract(data: list, row_start: int, row_stop: int, threshold: float) -> np.ndarray:
    data = np.array(data, dtype = np.float64)
    block = data[row_start:row_stop]
    filter = block[block > threshold]
    return np.array(filter, dtype = np.float64)
    
