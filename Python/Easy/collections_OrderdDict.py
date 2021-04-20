from collections import OrderedDict

dictionary = OrderedDict()
for i in range(int(input())):
    order, space, price = input().rpartition(' ')
    if order not in dictionary.keys():
        dictionary[order] = int(price)
    else:
        dictionary[order] += int(price)

for key, value in dictionary.items():
    print(key, value)
