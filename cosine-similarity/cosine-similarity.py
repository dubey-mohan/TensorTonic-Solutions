import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a = np.array(a)
    b = np.array(b)
    dot = float(a @ b)
    mod_a, mod_b = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if mod_a == 0 or mod_b == 0:
        return 0.0
    return dot / (mod_a * mod_b)
    

    