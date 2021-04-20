import numpy

n, m = map(int, input().split())
print(str(numpy.eye(n, m)).replace('0', ' 0').replace('1', ' 1'))
