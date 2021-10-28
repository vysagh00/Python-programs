import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])


b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b[1,2])

a = np.zeros((4,4))
print(a)

a = np.ones((4,2))
print(a)

a = np.full((4,2),254)
print(a)

a = np.eye(3)
print(a)

a = np.random.random((2,2))
print(a)

a = np.random.randint(2,100,(2,2))
print(a)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(np.add(x,y))

print(np.dot(x,y))