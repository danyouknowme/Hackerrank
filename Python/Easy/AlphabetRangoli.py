def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    data = [alpha[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(size*4-3, "-"))
