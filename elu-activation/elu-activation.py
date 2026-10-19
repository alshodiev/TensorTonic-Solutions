import math
import numpy as np


def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    x_con = np.asarray(x, dtype = float)
    return list(np.where(x_con < 0, alpha * (np.exp(x_con) - 1), x_con))
    