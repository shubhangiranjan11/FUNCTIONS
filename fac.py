def factorial(num):
    factorial=1
    while num>0:
        factorial=factorial*num
        num=num-1
    print(factorial,"factorial")
num=int(input("any number"))
factorial(num)