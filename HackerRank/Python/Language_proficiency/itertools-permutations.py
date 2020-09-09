from itertools import permutations
a, n = input().split()
print(*[''.join(i) for i in permutations(sorted(a),int(n))],sep='\n')