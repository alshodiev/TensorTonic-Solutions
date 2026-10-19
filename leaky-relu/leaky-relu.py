import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    """
    x_con = np.asarray(x, dtype = float)
    for i in range(len(x_con)):
        if x_con[i] < 0:
            x_con[i] *= alpha
    return x_con
    """
    x_con = np.asarray(x, dtype = float)
    return np.where(x_con < 0, alpha * x_con, x_con)
    