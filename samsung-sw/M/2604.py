
def getTC():
    count = int(input())
    return count

def getOffsetLength(length):
    for i in range(length):
        getOffset(int(input()))
    
def getOffset(length):
    offsetList = []
    for i in range(length):
        a,b = map(int, input().split())
        offsetList.append([a, b])
    findLargestOffsets(offsetList)

def findLargestOffsets(list):
    offsetList = sorted(list)
    print("offsetList {}".format( offsetList))
    whileIndex = 0
    while True:
        a = offsetList[whileIndex]
        c = offsetList[(len(offsetList) - 1) - whileIndex]
        for value in offsetList:
            if([abs(c[0]),abs(a[1])] == [abs(value[0]), abs(value[1])]):
                b = [value[0],value[1]]
                setExtend(a,b,c)
                break
        else:
            whileIndex += 1
        break

    for i in result:
        print(i)

def setExtend(a, b, c):
    underLine = b[0] - a[0]
    sideLine = c[1] - b[1]
    result.append(underLine * sideLine)
    
                
result = []
getOffsetLength(getTC())

