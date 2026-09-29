len = int(input())
result = 0
for _ in range(len):
    value = list(input())
    cacheValue = []
    itemResult = True
    for i in value:
        if cacheValue.count(i) == 0:
            cacheValue.append(i)
        elif(cacheValue[-1] == i):
            continue
        else :
            itemResult = False
            break 
    if itemResult : result+=1
print(result)
            