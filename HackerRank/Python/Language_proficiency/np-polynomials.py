import numpy as np
c = list(map(float, input().split()))
print(np.polyval(c, int(input())))