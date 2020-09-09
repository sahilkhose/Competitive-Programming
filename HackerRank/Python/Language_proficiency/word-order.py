from collections import OrderedDict
od = OrderedDict()

for i in range(int(input())):
    word = input()
    od.setdefault(word, 0)
    od[word] +=1
print(len(od))
print(*od.values())