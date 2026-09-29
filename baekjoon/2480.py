a, b, c = map(int, input().split())
if a == b and b == c and c == a : 
    print(10000 + 1000 * a)
elif a == b :
    print(1000 + 100* a)
elif c == b :
    print(1000 + 100* b)
elif a == c :
    print(1000 + 100* a)
else:
    max= max([a,b,c])
    print(max * 100)