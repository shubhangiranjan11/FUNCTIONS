def check_numbers():
    list1=[2,6,18,10,3,75]
    list2=[6,19,24,12,3,87]
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print(list1[i],list2[i],"dono even hai")
        else:
            print(list1[i],list2[i],"dono odd hai")
        i=i+1
check_numbers()