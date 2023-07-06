password=121314
username=222324
a=int(input("please enter your password"))
b=int(input("please enter your username"))
if password == a and username==b:
    print("میتونی وارد شی")
else: 
    print("دوباره تلاش کن")
    a=int(input("please enter your password"))
    b=int(input("please enter your username"))
    
    if password == a and username==b:
        print("میتونی وارد شی")
    else: 
        print("نمی توانی وارد شوی")