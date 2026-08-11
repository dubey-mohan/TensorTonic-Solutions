import numpy as np

def sigmoid_squeeze_analysis(x):
    """
    Returns: dict with 'bounds' (list of [lower, sigmoid, upper] triples) and 'is_saturated' (list of bools)
    """
    o = {'bounds': [], 'is_saturated': []}

    for val in x:
        l_bound  = max(0, 1 - np.exp(-val))
        u_bound = min(1, np.exp(val))
        sig = 1 / (1 + np.exp(-val))

        o['bounds'].append([l_bound, sig, u_bound])

        if min(sig, 1 - sig) < 1e-4:
            o['is_saturated'].append(True)
        else:
            o['is_saturated'].append(False)

    return o
            
