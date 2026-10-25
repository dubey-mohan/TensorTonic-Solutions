import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed = seed)
    if kind == 'normal':
        return rng.standard_normal(shape)
    else:
        return rng.random(shape)
        
    
