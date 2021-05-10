def show_number(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i=i+1
limit=int(input("any number"))
show_number(limit)