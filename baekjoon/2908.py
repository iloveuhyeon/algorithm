alphabet = input()
result = []
for value in alphabet:
    if(value  == "A" or value  ==  "B" or value  == "C"):
        result.append(0)
    elif(value  == "D" or value  ==  "E"or value  ==  "F"):
        result.append(1)
    elif(value  == "G" or value  ==  "H"or value  ==  "I"):
        result.append(2)
    elif(value  == "J" or value  ==  "K"or value  ==  "L"):
        result.append(3)
    elif(value  == "M" or value  == "N"or value  == "O"):
       result.append(4)
    elif(value  == "P" or value  ==  "Q"or value  ==  "R" or value  ==   "S"):
        result.append(5)
    elif(value  == "T" or value  ==  "U"or value  ==   "V"):
        result.append(6)
    elif(value  == "W" or value  ==  "X"or value  ==  "Y"or value  ==  "Z"):
        result.append(7)
    else:
        result.append(8)
print(sum(result) + 3 * len(result))