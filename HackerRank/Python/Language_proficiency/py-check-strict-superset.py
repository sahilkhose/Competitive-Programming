a = set(map(int, input().split()))
for _ in range(int(input())):
    b = set(map(int, input().split()))
    if(len(a.intersection(b)) != len(b)):
        print("False")
        exit()
print("True")