"""
i: x
o: y (int)
"""

import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x_con = np.asarray(x, dtype=float)
    num = 1
    denum = 1 + np.exp((-1) * x_con)

    return num/denum
    