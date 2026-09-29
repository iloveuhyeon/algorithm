all = int(input())
len = int(input())
costList = []
for i in range(len):
    cost, costLen = map(int, input().split())
    costList.append([cost, costLen])
allCost = 0
for i in costList:
    allCost += i[0] * i[1]
if(allCost == all):
    print("Yes")
else:
    print("No")