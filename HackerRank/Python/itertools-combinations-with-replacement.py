from itertools import combinations_with_replacement
a, n = input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(a),int(n))],sep='\n')