text=input('enter your text')
a=0
for char in text:
    if char.isdigit():
        a+=int(char)
        print(a)