def append():
    i=0
    b=[]
    while i<len(string_list):
        if string_list[i] not in b:
            b.append(string_list[i])
        i=i+1
    print(b)
string_list=["rishab","rishab","abhishek","rishab","divyansh","divyansh"]
append()

