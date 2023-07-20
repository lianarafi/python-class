import random
x=int(input('enter your len list'))
start=int(input('enter the start of the range:'))
end=int(input('enter the end of the range:'))
random_list=random.sample(range(start,end),x)
print(random_list)
