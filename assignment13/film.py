def show_menu(menu):
    print('1.add filme')
    print('2.show list')
    print('3.show best film')
    print('4.show films in alphabetical order')
    print('5.exit')
show_menu('menu')

x=int(input('choose a number'))
a=[]
b=[]
if x==5:
    print('good bye')
if x==1:
    z=input('enter the name of the movie')
    s=input('enter the movie score')
    a.append(z)
    a.append(s)
    b.append(z)
    show_menu('menu')
    x=int(input('choose a number'))
    while True:
        if x==1:
            m=input('enter the name of the movie')
            d=input('enter the movie score')
            a.append(m)
            a.append(d)
            b.append(m)
            show_menu('menu')
            x=int(input('choose a number'))
        else:
            break

if x==2:
    print(a)
    show_menu('menu')
    x=int(input('choose a number'))
    while True:
        if x==2:
            print(a)
        else:
            break

if x==3:
    t=a[1] 
    v=a[3]
    q=a[5]
    w=a[7]
    k=a[9]
    e=[]
    e.append(t)
    e.append(v)
    e.append(q)
    e.append(w)
    e.append(k)
    e.sort()
    e.reverse()
    print(e)

if x==4:
    u=a[0]
    p=a[2]
    g=a[4]
    j=a[6]
    l=a[8]
    f=[]
    f.append(u)
    f.append(p)
    f.append(g)
    f.append(j)
    f.append(l)
    f.reverse()
    f.sort()

    print(f)