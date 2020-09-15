from itertools import groupby
key_and_group = []
for key, group in groupby(input()): 
    key_and_group.append((len(list(group)), int(key)))
print(*key_and_group) 

# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])