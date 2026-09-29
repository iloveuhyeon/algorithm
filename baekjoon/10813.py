import sys
input = sys.stdin.readline

studentList = list(range(1,31))
for _ in range(len(studentList) - 2) : studentList.remove(int(input()))
print("{}\n{}".format(studentList[0],studentList[1]))