n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    inp = input().split()
    if(inp[0] == "pop"):
        s.pop()
    elif(inp[0] == "discard" or inp[0] == "remove"):
        s.discard(int(inp[1]))
print(sum(s))
