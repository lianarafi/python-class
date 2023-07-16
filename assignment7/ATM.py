password = '1234'
password_list = [password[0],password[1],password[2],password[3]]
c = 0

while c < 3:
    i_password = input("enter your password -> ")
    
    if len(i_password) == 4:
        if password == i_password:
            print("welcome")
           
        elif str([i_password[0],i_password[1],i_password[2],i_password[3]]) == str(password_list[::-1]):
            print("Calling the police!!!")
        
        
        else:
            print("egain")
            c += 1
    
    else:
        print("try again")

print("You cant enter")
  




