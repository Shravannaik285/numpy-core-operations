# utils.py
import numpy as np

# Arithmetic operations
def add_arrays(a, b):
    return np.add(a, b)

def sub_arrays(a, b):
    return np.subtract(a, b)

def mul_arrays(a, b):
    return np.multiply(a, b)

def div_arrays(a, b):
    return np.divide(a, b)

# Difference operations
def difference_array(a):
    return np.diff(a)

# Aggregations
def total_sum(a):
    return np.sum(a)

def total_product(a):
    return np.prod(a)
