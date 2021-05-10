def fun(num):
    i=0
    while i<=num:
        if i%3==0 and i%7==0:
            print(i,"nav")
        elif i%3==0:
            print(i,"gurukul")
        elif i%7==0:
            print(i,"navgurukul")
        i+=1
num=int(input("any number"))
fun(num)