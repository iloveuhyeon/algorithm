import sys
input = sys.stdin.readline
n,m = map(int, input().split())
basket = list(range(1, n +1))
for _ in range(m):
    i, j = map(int, input().split())
    subBasket= basket[ (i - 1) : (j )]
    subBasket.reverse()
    basket[(i - 1) : (j)] = subBasket
print(*basket)
    