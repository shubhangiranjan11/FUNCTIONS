def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"maximum")
    elif num2>num1 and num2>num3:
        print(num2,"maximum")
    elif num3>num1 and num3>num2:
        print(num3,"maximum")
    else:
        print("euqal")
num1=int(input("any number"))
num2=int(input("any number"))
num3=int(input("any number"))
max(num1,num2,num3)

