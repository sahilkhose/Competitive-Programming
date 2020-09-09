if __name__ == '__main__':
    name = []
    score = []
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))

    min = sorted(list(set(score)))[1]
    name = sorted([name[idx] for idx, sc in enumerate(score) if sc==min])
    [print(n) for n in name]