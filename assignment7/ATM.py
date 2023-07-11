password=1234
password_list=[password[1],password[2],password[3]]
a=0
while a<3:
    num=int(input("enter your password"))
if len(num)==4:
    if password==num:
        print("welcom")
    elif str([num[0],num[1],num[2],num[3]])==str(password_list[::-1]):
        print("caling the police")
    else:
        print("try egain")
    a+=1
else:
    print("try egain")

    print("you cant enter") 


  




