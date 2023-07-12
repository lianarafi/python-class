string=input("enter your sentence:")
string=string.split()
string="".join(string)
a=-1
for i in range(len(string)//2):
    if string[i] !=string[a]:
        print("no")

else:
    a+=-1
    print("yes")