from numpy import *

a1 = arange(1, 10)
a2 = a1.copy()

a2[3] = 40

print('a1', a1)
print('a2', a2)