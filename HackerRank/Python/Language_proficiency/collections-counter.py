from collections import Counter
input()
shoe = map(int, input().split())
shoe_count = Counter(shoe)
earn = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if(shoe_count[size]):
        shoe_count[size] -= 1
        earn += price
print(earn)