from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
list1 = []

for i in range(1, n+1):
    d[input()].append(str(i))

for i in range(m):
    x = input()
    if x in d:
        print(" ".join(d[x]))
    else:
        print(-1)
