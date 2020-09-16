n, x = map(int, input().split())
st = []
[st.append(map(float, input().split())) for _ in range(x)]
[print(sum(k)/x) for k in zip(*st)]