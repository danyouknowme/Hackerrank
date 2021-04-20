setA = set(map(int, input().split()))
setB = set()
for i in range(int(input())):
    otherSet = set(map(int, input().split()))
    setB.update(otherSet)
print(setA.issuperset(setB))
