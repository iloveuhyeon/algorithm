for TC in range(1, 1 + int(input())):
    order = list(map(int, input().split()))
    result = 0
    for value in order:
        result += value / 100
    print(f"#{TC} {int(result)}")