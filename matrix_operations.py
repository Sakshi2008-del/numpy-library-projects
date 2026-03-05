import numpy as np

a = np.array([[3,6],[4,9]])
b = np.array([[3,7],[8,2]])

addition = a + b
mutiplication = np.dot(a,b)
transpose = np.transpose(a)
mean_a = np.mean(a)
max_a = np.max(a)

print("matrix a : \n", a)
print("matrix b : \n", b)

print("\n addition :\n",addition)
print("\n multiplication :",mutiplication)
print("\n transpose :\n",transpose)

print("\n mean of a :", mean_a)
print("\n max value in a :", max_a)
