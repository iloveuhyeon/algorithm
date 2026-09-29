n, m = map(int, input().split())
matrix = []
for i in range(n):
    value = list(map(int,input().split()))
    matrix.append(value)
for i in range(n):
    value = list(map(int,input().split()))
    for j, valueItem in enumerate(value):
        matrix[i][j] += valueItem
for i in matrix:
    print(*i)
