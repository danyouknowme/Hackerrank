n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(1, len(arr)):
    if arr[i] != arr[0]:
        print(arr[i])
        break
