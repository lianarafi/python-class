numbers=list()
numbers2=[]
num=0
for i in range(10):
    number=int(input("enter your number:"))
    numbers.append(number)

while num<len(number):
    numbers2=numbers[num]+2
    num+1
    num.append(num)

print(numbers)
print(num)
