def divisible(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0 and i%5==0:
            sum=sum+i
        i=i+1
        print(sum)
limit=int(input("any number"))
divisible(limit)


