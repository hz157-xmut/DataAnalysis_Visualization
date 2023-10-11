import numpy as np
data = np.genfromtxt(r'C:\Users\horiz\1\score1.txt', dtype=str, delimiter=',', skip_header=1)
modified_student_ids = []
for student_id in data[:, 0]:
    modified_id = '2019' + student_id[4:] if student_id.startswith('2017') else student_id
    modified_student_ids.append(modified_id)
data[:, 0] = modified_student_ids
scores = data[:, 2:].astype(int)
average_scores = np.mean(scores, axis=0)
print(data)
print("平均分:")
print(average_scores)