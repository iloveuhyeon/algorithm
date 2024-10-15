a = input() 
b = []

for i in range(int(a)):
    b.append(input())



b = list(set(b))

b = sorted(b)
b.sort(key=len)

print('\n'.join(b))