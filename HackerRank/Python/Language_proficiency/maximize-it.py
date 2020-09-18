from itertools import product
k, m = map(int, input().split())
li = [list(map(int, input().split()[1:])) for _ in range(k)]
print(max(list(map(lambda x: sum(i**2 for i in x)%m, product(*li)))))