import numpy as np

def dot_product(x: list, y: list) -> float:
    x = np.array(x)
    y = np.array(y)
    ans = x @ y
    return float(ans)