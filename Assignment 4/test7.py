a=int(input("enter your weight"))
b=int(input("enter your height"))
mbi=a//b*b
if mbi<= 18.5:
    print("کمبود وزن")
elif 18.5<=mbi<=24.9:
    print("وزن نرمال")
elif 24.9<=mbi<=29.9:
    print("اضافه وزن")
elif mbi>30:
    print("چاقی")



