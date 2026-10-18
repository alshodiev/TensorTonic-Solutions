"""
i: x (list)
o: y (list)
"""

import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    
    """
    prev solution
    
    # check if its a scalar
    if np.ndim(x) == 0:
        return np.max(0, x)
    else:
        # check if its 2d array
        if len(x) != 1 and len(x[0]) != 1:
            for i in range(len(x)):
                for j in range(len(x[0])):
                    x[i][j] = np.max(0, x[i][j])
        else:
            # if its not 2d, then its 1d array
            if len(x) != 1:
                for i in range(len(x)):
                    x[i] = np.max(0, x[i])
    return np.asarray(x, dtype = float)
    """
    x_con = np.asarray(x, dtype = float)
    return np.maximum(0, x_con)
        
        
        
        
    
    