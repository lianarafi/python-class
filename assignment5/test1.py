number=int(input("enter your number"))
even='number'.count(1)+'number'.count(3)+'number'.count(5)+'number'.count(7)+'number'.count(9)
odd='number'.count(0)+'number'.count(2)+'number'.count(4)+'number'.count(6)+'number'.count(8)
if even>odd:
    print(even)
elif even<odd:
    print(odd)
else:
    print("barabar")