std = []
N = int(input())
idx = (input().split()).index("MARKS")
[std.append(int(input().split()[idx])) for i in range(N)]
print(f"{sum(std)/N :.2f}")