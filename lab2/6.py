def DoublePower(a, n):
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans *= a
    return(ans)
//В задании только функцию написать
