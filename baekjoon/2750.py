value = list()
for _ in range(int(input())):
    value.append(int(input()))
value.sort()
print(*value, sep="\n")