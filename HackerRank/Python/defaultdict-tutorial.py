# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    for idx in range(n):
        d[str(input())].append(idx+1)
    for j in range(m):
        print(*d[input()] or [-1])