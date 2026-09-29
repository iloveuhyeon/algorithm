import sys
input = sys.stdin.readline
subjectLen = int(input())
subjectList  = list(map(int, input().split()))
maxScore = max(subjectList)
for index, value in enumerate(subjectList):
    subjectList[index] = value / maxScore * 100
print(sum(subjectList)/ subjectLen)
