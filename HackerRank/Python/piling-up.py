import collections
for no_tests in range(int(input())):
    no_cubes = int(input())
    d = collections.deque([int(ele) for ele in input().split()])
    var = max(d)
    if(max(d) == d[-1]):
        var = d.pop()
    else:
        var = d.popleft()
    while(len(d)):
        max_idx = d.index(max(d[0], d[-1]))
        min_idx = d.index(min(d[0], d[-1]))

        if(d[max_idx] <= var):
            if(d[max_idx] == d[-1]):
                var = d.pop()
            else:
                var = d.popleft()
        elif(d[min_idx] <= var):
            if(d[min_idx] == d[-1]):
                var = d.pop()
            else:
                var = d.popleft()

        else:
            break

    if(len(d) == 0):
        print("Yes")
    else:
        print("No")
