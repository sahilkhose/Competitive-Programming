from collections import OrderedDict
od = OrderedDict()
for _ in range(int(input())):
    name, _, price = input().rpartition(" ")
    od[name] = od.get(name, 0) + int(price)
for item, quantity in od.items():
    print(item, quantity)