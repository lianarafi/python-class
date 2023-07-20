import random

Animals=['cat','dog','kitten','cow','puppy','turtle','rabbit','mouse','fish','hhamster','pig','sheep'
'deer','goat','crab','dove','stork','hawk','swan','own','mole','fox']

city=['mashad','tehran','esfahan','shiraz','yazd','gilan','kordestan','rasht','kashan',]

colers=['red','green','blue','dark red','brown','black','yellow','pink','silver','purple','navy blue',
'orange','maroom','charcoal','coral','beige']

country=['iran','china','cyprus','denmark','eqypt','finland','france','germany','iraq','italy','malaysia'
'mexico']

flowers=['carnation','iris','lily','peony','petunia','rose','sun flower','tulip','violet','feverfew'
'hyacinth']

x=int(input("enter your subject number (1-flowers , 2-country, 3-colers, 4-city, 5-Animals)"))
if x == 1:
    z = flowers
elif x == 2:
    z = country
elif x == 3:
    z = colers
elif x == 4:
    z = city
else:
    z = Animals
word=random.choice(z)
hearts=(len(word))*2
show=[]
for i in range(len(word)):
    show.append('_')
while True:
    print('_'.join(show))
    print('❤️'*int(hearts))
    if not('_'in show): 
        print('you win')
        break
    elif hearts==0:
        print('game over')
        break
    z=input('enter character')
    if z in word:
        idx=word.index(z)
        show[idx]=z
        letters='abcdefghijklmnopqrstuvwxyz'
        n=0
        x=[]
        print('you have already guessed this letter. please choose another one')

    else:
        print('this is not exist')
        hearts-=1