from numpy import *

a1 = array([1,2,3,4,5,6])
a2 = array([[1,2,3],[4,5,6]])
a3 = array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12.13121312]]])

print(a1)
print(a2)
print(a3)

print('--dimension--')
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print('--shape--')
print('a1', a1.shape)
print('a2', a2.shape)
print('a3', a3.shape)

#a2.shape = (3,2)
#print(a2)

print('--size--')
print(a1.size)
print(a2.size)
print(a3.size)

print('--itemsize--')
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

print('--datatype--')
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

print('--bytes--')
print(a1.nbytes)
print(a2.nbytes)
print(a3.nbytes)