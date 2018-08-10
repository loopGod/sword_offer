def Fibonacci(n):
    if n == 1 or n ==2:
        return 1
    s=[1,1]
    for i in range(2,n):
        s.append(s[i-1]+s[i-2])
    return s.pop()
print(Fibonacci(6))