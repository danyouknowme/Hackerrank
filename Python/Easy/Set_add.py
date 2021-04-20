result = set()
for i in range(int(input())):
    country = input()
    if country not in result:
        result.add(country)
print(len(result))
