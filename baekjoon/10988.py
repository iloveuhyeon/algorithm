import math
value = input()
centerIndex = math.floor((len(value)) / 2)
frontValue = value[:centerIndex]
backValue = value[centerIndex + 1 if len(value) % 2 == 1 else centerIndex::][::-1]
print(1 if frontValue == backValue else 0)