def var():
    list=[1,342,75,23,98]
    list1=[75,23,98,12,78,10,1]
    b=[]
    i=0
    while i<len(list):
        if list[i] in list1:
            b.append(list[i])
        i=i+1
    print(b)
var()