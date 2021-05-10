def harshad():
    sum=0
    num=0
    rem=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    if num%sum==0:
        print("harshad number")
    else:
        print("not harshad number")
num=int(input("any number"))
harshad()