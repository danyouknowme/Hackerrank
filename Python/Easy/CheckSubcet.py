for i in range(int(input())):
    sizeA, setA = int(input()), set(map(int, input().split()))
    sizeB, setB = int(input()), set(map(int, input().split()))
    print(setA.issubset(setB))
