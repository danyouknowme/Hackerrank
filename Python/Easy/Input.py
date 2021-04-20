var, result = map(int, input().split())
condition = input()
condition = condition.replace('x', str(var))
x = [True if eval(condition)==result else False]
print(x[0])
