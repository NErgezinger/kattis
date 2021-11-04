import sys
from math import log10, ceil
i = 1
for n in sys.stdin:
    n = int(n)

    circ_exponent = log10(3) + (n * log10(3/2))
    num_digits = ceil(circ_exponent)

    print("Case " + str(i) + ": " + str(num_digits))
    i+=1