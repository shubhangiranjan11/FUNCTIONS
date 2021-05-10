def perfect_num():
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+1
        i=i+1
    if sum==n:
        print(i,"perfect number")
    else:
        print(i,"not perfect number")
n=int(input("any number"))
perfect_num()


