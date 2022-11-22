a = int(input())
b = int(input())
c = int(input())
d = 0
if (a == b) and (a == c):
    d = 3
if a == c and a != b or a == b and a != c:
    d = 2

print(d)
