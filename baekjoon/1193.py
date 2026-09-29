num = int(input())
index = 0
while num > index * (index + 1) / 2:
    index += 1
diff = index * (index + 1) / 2 - num
if(index %2 == 1):
    print(int(diff+ 1),"/",int(index -diff),sep="")
else : 
    print(int(index -diff),"/",int(diff+ 1),sep="")