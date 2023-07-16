import random

num=random.randint(1,100)

while True:
    user_number=int(input("user_number: "))
    if user_number==num:
        print("afarin")
        break
    elif user_number>num:
        print("payintar")
    elif user_number<num:
        print("balatar")