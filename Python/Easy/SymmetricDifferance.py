sym_diff = set()
M = int(input())
valueOfM = set(map(int, input().split()))
N = int(input())
valueOfN = set(map(int, input().split()))
sym_diff.update(valueOfM.difference(valueOfN))
sym_diff.update(valueOfN.difference(valueOfM))
for s in sorted(sym_diff):
    print(s)
