import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:

    data = np.array(data, dtype = np.float64)

    element_mask = (data > threshold).astype(np.float64)
    
    any_row_mask = np.any(data > threshold, axis = 1)
    any_row_filter = data * any_row_mask[:, np.newaxis]
    
    all_row_mask = np.all(data > threshold, axis = 1)
    all_row_filer = data * all_row_mask[:, np.newaxis]
    
    return np.array([element_mask, any_row_filter, all_row_filer],
                    dtype = np.float64
                   )
    
    
