print('1.sum')
print('2.minus')
o=int(input('choose one'))
if o==1:
    m=int(input('enter  first daqiqe'))
    s=int(input('enter  first sait'))
    mm=int(input('enter secend daqiqe'))
    ss=int(input('enter secend sait'))
    l=m+mm
    ll=s+ss
    if l>60:
        n=l%60
        nn=l//60
        nnn=ll+nn
        print(nnn)
        print(':')
        print(n)
    else:
        print(ll)
        print(":")
        print(l)
if o==2:
    h=int(input('enter  first miment'))
    k=int(input('enter  first sait'))
    hh=int(input('enter secend daqiqe'))
    kk=int(input('enter secend sait'))
    f=h-hh
    g=k-kk
    print(f)
    print(':')
    print(g)

