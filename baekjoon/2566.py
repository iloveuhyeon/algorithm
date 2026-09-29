matrix = []
max = [0,1,1]
for _ in range(9):
    matrix.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if(max[0] < matrix[i][j]):
            max[0] = matrix[i][j]
            max[1] = i + 1
            max[2] = j + 1
print(max[0])
print(max[1],max[2])