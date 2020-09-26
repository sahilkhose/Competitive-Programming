from itertools import combinations
a, n = input().split()
for num in range(1, int(n)+1):
    print(*[''.join(i) for i in combinations(sorted(a), num)],sep='\n')