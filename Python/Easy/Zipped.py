x, y = map(int, input().split())
a = [float(x) for x in input().split()]
x = [a]
for i in range(y-1):
    llist = [float(x) for x in input().split()]
    x += [llist]
for i in list(zip(*x)):
    print("{:2f}".format(sum(i) / y))
