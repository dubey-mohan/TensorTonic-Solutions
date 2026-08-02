import numpy as np
import sympy as sp

def lr_schedule_analysis(alpha_0, k):

    limit = 0.0 if k > 0 else float(alpha_0)
    sum_diverges = alpha_0 > 0
    sum_sq_converges = (k > 0) or (alpha_0 == 0)
    
    return {
        'limit': limit,
        'sum_diverges': sum_diverges,
        'sum_sq_converges': sum_sq_converges
    }

    

    
    

    
    

