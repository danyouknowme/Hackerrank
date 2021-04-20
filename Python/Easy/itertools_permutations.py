from itertools import permutations

getInput = input().split(' ')
word = getInput[0]
step = int(getInput[1])

per = sorted(list(permutations([x for x in word], step)))
for i in range(len(per)):
    print("".join(per[i]))
