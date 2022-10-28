from collections import deque

n, m = map(int, input().split())
tax = [0] * (m + 1)
house = [0] * (n + 1)
amount = 0
for i in range(1, m + 1):
    t, h = map(int, input().split())
    tax[i] = t
    house[h] = i

idx = 1
while house[idx] == 0:
    idx += 1

q = deque()

for i in range(idx, n + 1):
    if house[i] == 0:
        t = q.popleft()
        amount += tax[t]
        q.append(t)
    else:
        amount += tax[house[i]]
        q.append(house[i])

print(amount)
