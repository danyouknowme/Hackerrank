from collections import Counter

numShoes = int(input())
shoes = Counter(list(map(int, input().split(' '))))
numCus = int(input())


income = 0 
for i in range(numCus):
    size_wanted, price = map(int, input().split(' '))
    for size, amount in shoes.items():
        if size_wanted == size:
            if amount > 0:
                income += price
                shoes[size] = amount - 1
print(income)
