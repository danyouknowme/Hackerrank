thickness, length = map(int, input().split())
c = ".|."
for i in range(1, thickness, 2):
    print((c*i).center(length, "-"))

print("WELCOME".center(length, "-"))

for i in range(thickness-2, 0, -2):
    print((c*i).center(length, "-"))
