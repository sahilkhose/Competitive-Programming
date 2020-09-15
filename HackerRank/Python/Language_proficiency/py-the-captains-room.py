k = int(input())
rooms = input().split()
s1 = set()
s2 = set()

for room in rooms:
    if room in s1:
        s2.add(room)
    else:
        s1.add(room)
print(*s1.difference(s2)) 
