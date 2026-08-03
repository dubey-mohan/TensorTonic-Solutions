import numpy as np

def activation_continuity_analysis(x):

    output = {
        "relu": [],
        "leaky_relu": [],
        "gelu": []
    }

    for val in x:
        if val == 0.0:
            output["relu"].append(0.0)
            output["leaky_relu"].append(0.0)

    return output
        
        

        



    
    
    
