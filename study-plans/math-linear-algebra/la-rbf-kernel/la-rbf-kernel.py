import numpy as np

def rbf_kernel_matrix(X, gamma):

    X = np.array(X)
    rows = X.shape[0]
    K = np.zeros((rows, rows))
    

    for i in range(rows):
        for j in range(i, rows):

            diff = X[i] - X[j]
            sq_diff = np.sum(diff ** 2)
            value = np.exp(-gamma * sq_diff)
            
            K[i, j] = value
            K[j, i] = value


    return K
            

            

    
        
        
        

    
                
            
           
                

            
                
    
    

    

    
                

            
            
            

    
    