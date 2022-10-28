# Rare Number

N = int(input())
A = map(int, input().split())

count = {}

for a in A:
    count.setdefault(a, 0)
    count[a] += 1
    print(count)

print(sorted(count.items(), key=lambda x: (x[1], x[0]))[0][0])