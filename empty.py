def empty():
    i=0
    empty=[]
    while i<len(list1):
        if list1[i] not in empty:
            empty.append(list1[i])
        i=i+1
        print(empty)
list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
print(list1)
empty()