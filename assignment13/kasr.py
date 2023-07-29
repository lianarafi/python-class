print('1.sum')
print('2.minus')
print('3.nultiply')
print('4.division')
o=int(input('choose one'))
if o==1:
    num1=int(input('enter your first sorat'))
    num2=int(input('enter your first makhrag'))
    nu1=int(input('enter your secend sorat'))
    nu2=int(input('enter your secend makhrag'))
    if nu2==num2:
        c=num1+nu1
        b=nu1
        print(c)
        print('___')
        print(nu2)
        print()
    else:
        n=num1*nu2
        nn=num2*nu2
        v=nu1*num2
        vv=nu2*num2
        nnn=n+v
        print(nnn)
        print('___')
        print(vv)
        print()
if o==2:
    na1=int(input('enter your first sorat'))
    na2=int(input('enter your first makhrag'))
    nna1=int(input('enter your secend sorat'))
    nna2=int(input('enter your secend makhrag'))
    if nna2==na2:
        d=na1-na2
        b=nna2
        print(d)
        print('___')
        print(nna2)
        print()
    else:
        l=na1*nna2
        ll=na2*nna2
        k=nna1*na2
        kk=nna2*na2
        www=l-k
        print(www)
        print('___')
        print(kk)
        print()
if o==3:
    p=int(input('enter your first sorat'))
    pp=int(input('enter your first makhrag'))
    e=int(input('enter your secend sorat'))
    ee=int(input('enter your secend makhrag'))
    i=p*e
    ii=pp*ee
    print(i)
    print('___')
    print(ii)
if o==4:
    u=int(input('enter your first sorat'))
    uu=int(input('enter your first makhrag'))
    t=int(input('enter your secend sorat'))
    tt=int(input('enter your secend makhrag'))
    s=u*tt
    ss=uu*t
    print(s)
    print('___')
    print(ss)