#!/usr/bin/env python

import numpy as np

def div(f,g):
    '''
    Generator to calculate an arbitrary number
    of terms of a polynomial division 
    
    Specifically in a generating function f(x) / g(x)

    Example:
        f(x) = 1 / (1 - x - x**2)

    Yields:
        the fibonacci numbers!

    Encode:
        f as: [1,  0,  0]
        g as: [1, -1, -1]
    '''
    f = np.array(f)
    g = np.array(g)
    assert( len(f) == len(g) )
    
    while True:
        term = f[0] / g[0]
        yield term
        f = np.roll(f - (term * g), -1)

