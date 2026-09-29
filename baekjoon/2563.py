offsetList = list(list(map(int, input().split())) for _ in range(int(input())))
result = set()
for value in offsetList:
    for i in range(10):
        for j in range(10):
            result.add((value[0] + i, value[1] + j))
print(len(result))