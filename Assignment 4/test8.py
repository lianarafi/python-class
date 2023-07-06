number=float(input("enter your number"))
if number<0:
    print("d")

elif number%2==0:
    n=number//10
    n=number-n*10

if n>6:
    print("a")

else:
    print("c")