n = int(input())
x = 0
for i in range(n):
    a, b = list(map(float, input().split()))
    x += a*b
print(x)