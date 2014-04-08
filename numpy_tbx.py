import numpy as np

def mat1(var):
    # create a np.mat object from an existing pre-computed variable number
    t = np.mat('1.0')
    t[0] = var
    return t