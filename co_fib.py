def co_fib(n):
    v1=1
    v2=1
    if(n > 0): yield 1
    if(n > 1): yield 1
    while(n > 2):
        v3= v1 + v2
        v1= v2
        v2= v3
        yield v3
        n -= 1

#1 1 2 3 5 8 13 21...
i=1
for fib_value in co_fib(10):
    print(str(i) + '=>' + str(fib_value))
    i+=1
