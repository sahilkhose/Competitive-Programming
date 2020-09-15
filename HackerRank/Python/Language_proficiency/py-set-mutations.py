len_a = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    qry, len_ = input().split()
    b = set(map(int, input().split()))
    if(qry == "update"):
        a.update(b)
    elif(qry == "intersection_update"):
        a.intersection_update(b)
    elif(qry == "difference_update"):
        a.difference_update(b)
    elif(qry == "symmetric_difference_update"):
        a.symmetric_difference_update(b)

print(sum(a))
