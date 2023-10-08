import numpy as np

steps = np.random.choice([-1, 1], 2000)
distance = np.cumsum(steps) * 0.5
final_distance = distance[-1]
print("最终距离原点的距离:", final_distance, "米")
