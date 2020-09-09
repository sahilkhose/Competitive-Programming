if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        ins = input().split()
        if(ins[0] == "print"):
            print(l)
        elif(ins[0] == "insert"):
            l.insert(int(ins[1]), int(ins[2]))
        elif(ins[0] == "remove"):
            l.remove(int(ins[1]))
        elif(ins[0] == "append"):
            l.append(int(ins[1]))
        elif(ins[0] == "sort"):
            l.sort()
        elif(ins[0] == "pop"):
            l.pop()
        elif(ins[0] == "reverse"):
            l.reverse()
