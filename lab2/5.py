a = int(input())
b = []
while a != 0:
    b.append(a % 10)
    a //= 10
print(b, len(b))
ans = 0
for i in range(0, len(b)):
    ans += b[i] * (2**i)
print(ans)
