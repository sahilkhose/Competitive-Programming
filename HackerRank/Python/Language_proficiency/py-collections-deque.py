from collections import deque
d = deque()
for _ in range(int(input())):
    op, *args = input().split()
    getattr(d, op)(*args)
print(*d)