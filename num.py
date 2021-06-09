import numpy as np

"""
#rank_1 array
a = np.array([1,2,3,4])
print(a)
print(type(a))
print(a.shape)
print(a[0],a[1],a[2],a[3])

"""

"""
#rank_2 array

b = np.array([[1,2,3],[3,4,5]])   
#ls = [[1,2,3],[3,4,5]]
print(b)
print(b.shape)
print(b[1][1])
print(b[0,2])

"""
"""
#array 0f n rows and column of zero
b = np.zeros((100,100))
print(b)
"""
"""
b = np.full((4,5),1026)
print(b)
"""
"""
b = np.eye(3)
print(b)
"""
"""
b = np.random.randint(0,100,(10,10))
print(b)
"""
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

#print(np.divide(y,x))
#print(y/x)

#print(np.sqrt(x))

#for dot products of matrix
print(np.dot(x,y))