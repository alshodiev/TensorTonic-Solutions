import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    l, a = 1.0507009873554804934193349852946, 1.6732632423543772848170429916717
    return [l*v if v > 0 else (l * a * (math.exp(v) - 1)) for v in x]