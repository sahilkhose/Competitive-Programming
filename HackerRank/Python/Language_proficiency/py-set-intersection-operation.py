input()
eng = set(map(int, input().split()))
input()
fre = set(map(int, input().split()))
print(len(eng.intersection(fre)))