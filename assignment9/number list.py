list=input('enter a list of numbers').split()
dct={}
for num in list:
    if num in dct:
        dct[num]+=1
    else:
        dct[num]=1
print(dct)