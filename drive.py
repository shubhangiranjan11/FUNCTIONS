def drive():
    speed=int(input("any number"))
    if speed<70:
        print("ok")
    if speed>70:
        a=speed-70
        b=a//50
        if b>12:
            print("licesence suspend",b)
        else:
            print(b)
drive()