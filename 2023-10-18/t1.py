import pandas as pd

s = pd.Series(pd.np.random.randint(1,100,100))
# 整个Series
print(s)
# 索引
print(s.index)
# 判断空
print(s.empty)
# 维度值
print(s.ndim)
# 大小
print(s.size)
# 值
print(s.values)
# 前10个值
print(s.head(10))
# 后10个值
print(s.tail(6))
