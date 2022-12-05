a = int(input())
b = int(input())
if a % 2 != 0:
    a += 1
while a < b + 1:
    print(a, end = " ")
    a +=2
