def add(n1,n2):

    if(n2>0):
        return(n1+add(n1,(n2-1)))
    else:
        return 0

print(add(4,7))
