a= int(input())
homeLen = 1
time = 1
while  a > homeLen:
    time += 1
    homeLen += ( time-1 ) * 6
print(time)