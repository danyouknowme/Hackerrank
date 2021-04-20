n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    order = input().split()
    if order[0] == 'pop':
        s.pop()
    elif order[0] == 'remove':
        s.remove(int(order[1]))
    elif order[0] == 'discard':
        s.discard(int(order[1]))
print(sum(s))
