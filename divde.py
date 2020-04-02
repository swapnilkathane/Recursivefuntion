def fibo(n1):
    if(n1>1):
        return n1-1,fibo(n1-1)
    else:
       return 1

print(fibo(10))