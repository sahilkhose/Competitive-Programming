from collections import Counter

chars = Counter(input()).items()

for char, freq in sorted(chars, key=lambda k: (-k[1], k[0]))[:3]:
    print(char, freq)