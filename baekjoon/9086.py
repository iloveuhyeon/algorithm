import sys
input = sys.stdin.readline
for _ in range(int(input())):
    value = input().rstrip()
    print(value[0] + value[-1])