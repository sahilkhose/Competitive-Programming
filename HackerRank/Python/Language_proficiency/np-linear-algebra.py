import numpy as np
a = np.array([input().split() for _ in range(int(input()))], float)
print(round(np.linalg.det(a), 2))