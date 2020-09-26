from itertools import combinations

n = int(input())
group = input().split()
idx_set = set(out for out in range(n))
group_len = int(input())

comb = list(combinations(group, group_len))
filt = filter(lambda c: 'a' in c, comb)
print(len(list(filt))/len(comb))


# idx_com = list(combinations(idx_set, group_len))
# temp = []
# main = []
# for j in idx_com:
#     temp.clear()
#     for idx in j:
#         temp.append(group[idx])
#     main.append(tuple(temp))
# # print(main)
# count = 0
# for ele in main:
#     for idx, _ in enumerate(ele):
#         if(ele[idx] == 'a'):
#             count+=1
#             break
    
# print(count/len(main))