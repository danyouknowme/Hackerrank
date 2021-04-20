from itertools import product

A = map(int, input().split())
B = map(int, input().split())
result = list(product(A, B))
for x in result:
    print(x, end=' ')
