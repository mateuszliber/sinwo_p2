import math
import pytest
import numpy as np

def NWD(a, b):
    '''Method for computing the greatest common divisor of two numbers (a, b)'''
    if((a<0 or b<0) or (np.isnan(a) or np.isnan(b))):
        raise(ValueError)

    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    return a
