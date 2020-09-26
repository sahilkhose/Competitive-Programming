for _ in range(int(input())):
    a_num = int(input())
    a = set(map(int, input().split()))
    b_num = int(input())
    b = set(map(int, input().split()))
    print(len(a.intersection(b)) == len(a))