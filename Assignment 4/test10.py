import math
print("1.-")
print("2.+")
print("3.*")
print("4./")
print("5.log10")
print("5.|first number|+|secend number|")
print("6.pow(first number.secend number)")
print("7.sqrt(number)")
print("8.round(number)")

op=int(input("enter your operaction"))

if op==1:
    num1=float(input("first number"))
    num2=float(input("secend number"))
    print(num1-num2)
elif op==2:
    num1=float(input("first number"))
    num2=float(input("secend number"))
    print(num1+num2)
elif op==3:
    num1=float(input("first number"))
    num2=float(input("secend number"))
    print(num1*num2)
elif op==4:
    num1=float(input("first number"))
    num2=float(input("secend number"))
    print(num1/num2)
elif op==5:
    num=float(input("enter a number"))
    print(math.log10(num)) 
elif op==6:
    num1=float(input("first number"))
    num2=float(input("secend number"))
    print("|num1|+num2|")
elif op==6:
    num1=float(input("first number"))
    num2=float(input("secend number"))
    print(math.pow(num1.num2))
elif op==7:
    num=float(input("enter a number"))
    print(math.sqrt(num))
elif op==8:
    num=float(input("enter a number"))
    print("round.(num)")



