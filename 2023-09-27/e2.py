import numpy as np

matrix1 = np.tile(np.arange(5), (5, 1))

matrix2 = np.zeros((8, 8))
matrix2[1:-1, 1:-1] = 0
np.fill_diagonal(matrix2, 1)
matrix2[0, :] = 5
matrix2[-1, :] = 5
matrix2[:, 0] = 5
matrix2[:, -1] = 5

scores = np.random.normal(70, 5, 43)

print("矩阵1:")
print(matrix1)
print("\n矩阵2:")
print(matrix2)
print("\n随机分数:")
print(scores)
