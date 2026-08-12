import numpy as np

def softmax_stability_analysis(z):
    """
    Returns: dict with 'naive', 'stable' (lists of floats) and 'naive_has_issues' (bool)
    """
    z = np.asarray(z, dtype = float)
    
    m = np.max(z)
    d_naive = np.sum(np.exp(z))
    d_stable = np.sum(np.exp(z - m))
    o = {'naive': [], 'stable': [], 'naive_has_issues': False}
        
    for val in z:
        naive = np.exp(val) / d_naive
        stable = np.exp(val - m) / d_stable

        o['naive'].append(naive)
        o['stable'].append(stable)

    naive_val = np.asarray(o['naive'])
    
    if any((np.isnan(naive_val) | np.isinf(naive_val))):
        o['naive_has_issues'] = True

    return o
            
            
            