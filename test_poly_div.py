#!/usr/bin/env python

import itertools as it
from poly_div import div

def take( gen, N=10 ):
    out = []
    for x in it.islice(gen, 0, N):
        out.append(x)
    return out

f = [1,0]
g = [1,5]
print
print "1 / 1 + 5x"
print take(div(f,g))

f = [1,0]
g = [1,1]
print
print "1 / 1 + x"
print take(div(f,g))

f = [1,0,0]
g = [1,0,-1]
print
print "1 / 1 - x^2"
print take(div(f,g))

f = [1,0,0]
g = [1,0,1]
print
print "1 / 1 + x^2"
print take(div(f,g))

f = [1,0,0]
g = [1,-2,1]
print
print "1 / 1 - 2x + x^2"
print take(div(f,g))

f = [1,0,0,0]
g = [1,-3,3,-1]
print
print "1 / 1 - 3x + 3x^2 - x^3"
print take(div(f,g))
