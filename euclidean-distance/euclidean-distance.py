import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    x = np.array(x)
    y = np.array(y)
    ans = np.sum((x - y)**2)**0.5
    return float(ans)
    
   