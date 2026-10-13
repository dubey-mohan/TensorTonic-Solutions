import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    x = np.array(x)
    y = np.array(y)
    return float(np.sum(np.abs(x - y)))
   