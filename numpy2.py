import numpy as np

import time

import sys

s = range(1000)

sys.getsizeof(5)*len(s)

d= np.arange(1000)
print(d.size*d.itemsize)
