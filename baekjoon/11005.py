n, b = map(int, input().split())
result = ""
while True:
    n, x = divmod(n,b)
    if(x > 9):
        result = chr(x + 55) + result
    else:
        if(n == 0):
            if(x != 0):
                result = str(x) + result
            break
        else : 
            result = str(x) + result
print(result)