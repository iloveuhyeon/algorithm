import sys
result = []
for i in range(int(sys.stdin.readline().rstrip())) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result.append(a + b)
for i in result:
    print(i) 
