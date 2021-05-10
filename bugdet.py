def budget(amount,student):
    c=len(student)
    total=c*amount
    if amount<=50000:
        print(total,"under budget")
    else:
        print(total,"over budget")
amount=int(input("any numner"))
budget(amount,["rakesh","krishna","aditya","kajal","muskan","kashish"])



