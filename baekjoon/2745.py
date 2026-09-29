n, b = input().split()
n = list(n)
n.reverse()
b = int(b)
for i in range(len(n)):
    try:
        n[i] = int(n[i])
    except:
        n[i]  = ord(n[i]) -55
    n[i]= b**i * n[i]
print(sum(n))
