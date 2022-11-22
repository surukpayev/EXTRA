a = int(input())
b = int(input())
c = int(input())
d = 0
if b < a:
    d = a
    a = b
    b = d
if c < a:
    d = a
    a = c
    c = d
if c < b:
    d = b
    b = c
    c = d
print (a, b, c)
