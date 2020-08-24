import numpy as np
n, m = input().split()
print(str(np.eye(int(n), int(m))).replace('1', ' 1').replace('0', ' 0'))
