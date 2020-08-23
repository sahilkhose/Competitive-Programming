# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = input().split()
 
a = int(a)
b = int(b)

pattern = [(".|."*i).center(b, "-") for i in range(1, a, 2)]
wel = ["WELCOME".center(b, "-")]
final = pattern + wel + pattern[::-1]
a = "\n".join(final)
print(a)
