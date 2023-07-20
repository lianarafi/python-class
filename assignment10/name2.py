name=input('enter a list of file namrs:')
name=name.split(" ")
for name in name:
    f=0
    c=0
    if "." in name:
        p=name.split('.')
        for i in ("0","1","2","3","4","5","6","7","8","9"):
            if i in p[1]:
                print(f"ther is a number in the name")
                f+=1
                break
        if len(p[1])==1 or len(p[1])>3:
            print(f"the problem is in the number of letters")
            f+=1
        elif p[1]=='err':
            print(f"the name suffix  is equal to'err'")
            f+=1
        else:
            print(f"in name'.' not find")
        for i in ("0","1","2","3","4","5","6","7","8","9"):
            c+=name.split(i)
            if c>3:
                print(f"ther are more than 3 numbers in the name")
                f+=1
                break
        for i in ("0","1","2","3","4","5","6","7","8","9"):
            if name[0]==i:
                print(f"name name start with a number")
                f+=1
        if f==0:
            print(f"name ic acceptable")
        else:
            print(f"name is not  acceptable")