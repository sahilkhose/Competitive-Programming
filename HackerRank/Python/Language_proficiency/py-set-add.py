# s = set()
# for _ in range(int(input())):
#     s.add(input())
# print(len(s))
print(len(set(input() for _ in range(int(input())))))