input()
num = input().split()
print(all([int(ele) > 0 for ele in num]) and any([a == a[::-1] for a in num]))