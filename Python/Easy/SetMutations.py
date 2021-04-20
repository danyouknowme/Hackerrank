(_, A) = (int(input()), set(map(int, input().split())))
for i in range(int(input())):
    (order, B) = (input().split()[0], set(map(int, input().split())))
    getattr(A, order)(B)
print(sum(A))
