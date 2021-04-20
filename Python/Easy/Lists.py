N = int(input())
finished_list = []
for i in range(N):
    order = input().split()
    if order[0] == "append":
        finished_list.append(int(order[1]))
    elif order[0] == "insert":
        finished_list.insert(int(order[1]), int(order[2]))
    elif order[0] == "remove":
        for num in finished_list:
            if num == int(order[1]):
                finished_list.remove(num)
                break
    elif order[0] == "sort":
        finished_list.sort()
    elif order[0] == "pop":
        finished_list.pop()
    elif order[0] == "reverse":
        finished_list.reverse()
    elif order[0] == "print":
        print(finished_list)
