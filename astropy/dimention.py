import numpy as np
import astropy
from astropy.modeling.models import Guassion2D 
data = (gs(1, 150, 45, theta = 0.5), (x,y))
data += 0.01 * np.rand(500, 600)
csc = 0.9997
data[100, 300, 310] = csc
