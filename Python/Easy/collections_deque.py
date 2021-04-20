from collections import deque

d = deque()
for i in range(int(input())):
    order = input().split(' ')
    if order[0] == 'append':
        d.append(order[1])
    elif order[0] == 'appendleft':
        d.appendleft(order[1])
    elif order[0] == 'pop':
        d.pop()
    elif order[0] == 'popleft':
        d.popleft()
print(' '.join(d))
