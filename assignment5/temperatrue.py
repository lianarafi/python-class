print("1.f=C*1.8+32")
print("2.c=(f-32)/1.8")
print("3.k=c+273.15")
print("4 .k=(f+459.67)/1.8")
print("5.c=k-273.15")
print("6.f=k*1.8-459.67")
o=int(input("enter your number"))
if o==1:
    num1=float(input("enter c"))
    print(num1*1.8+32)
elif  o==2:
    num1=float(input("enter f "))
    print((num1-32)/1.8)
elif o==3:
    num1=float(input("enter c "))
    print(num1+273.15)
elif o==4:
    num1=float(input("enter F"))
    print((num1+459.67)/1.8)
elif o==5:
    num1=float(input("enter K "))
    print(num1-273.15)
elif o==6:
    num1=float(input("enter k" ))
    print(num1*1.8-459.67)
