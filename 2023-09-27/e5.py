import numpy as np

matrix = np.arange(100).reshape(10, 10)
subblocks = np.lib.stride_tricks.sliding_window_view(matrix, (3, 3))
print("原始矩阵:")
print(matrix)
print("\n提取的3x3区块:")
for block in subblocks:
    print(block)
