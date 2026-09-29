QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1
for _ in range(int(input())):
    value = int(input())
    quarterLen = 0
    dimeLen = 0
    nickelLen = 0
    pennyLen = 0
    quotient, remainder = divmod(value, QUARTER)
    quarterLen = quotient
    value = remainder
    quotient, remainder = divmod(value, DIME)
    dimeLen = quotient
    value = remainder
    quotient, remainder = divmod(value, NICKEL)
    nickelLen = quotient
    value = remainder
    quotient, remainder = divmod(value, PENNY)
    pennyLen = quotient
    value = remainder
    print(quarterLen,dimeLen,nickelLen,pennyLen)
