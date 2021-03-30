import astropy
from astropy.table import Table as ta
try:
    a = ta.read('photometry.dat', format = 'ascii.daophot')
except Exception:
    print('')
