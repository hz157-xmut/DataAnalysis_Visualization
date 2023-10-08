import numpy as np

grades = np.random.randint(1, 101, (43, 5))
mean_second_course = np.mean(grades[:, 1])
sum_eighth_student = np.sum(grades[7, :])
fail_count_third_course = np.sum(grades[:, 2] < 60)

print("成绩矩阵:")
print(grades)
print("\n第2门课程平均分:", mean_second_course)
print("第8个同学总分:", sum_eighth_student)
print("第3门课程不及格人数:", fail_count_third_course)
