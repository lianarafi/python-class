class square:
    def __init__(self,z):
        self.zel=z
    def masahat(self):
        return(self.zel*self.zel)
    def mohit(self):
        return(self.zel*4)
class Triangle(square):
        def __init__(self,q,e):
            self.qaede=q
            self.ertefa=e
        def mas(self):
            return(self.qaede*self.ertefa/2)
        def moh(self):
            return(self.qaede*3)
class pyramid(Triangle):
        def __init__(self, q, e,):
            self.qae=q
            self.er=e
        def masa(self):
            return(self.qae*self.er/2*3+self.qae)
z=int(input('enter your number'))
rec1=square(z)
print('masahat moraba:',rec1.masahat())
print('mohite moraba:',rec1.mohit())
q=int(input("enter qaede"))
e=int(input('enter your ertefa'))
mos=Triangle(q,e)
print('mohit mosalas:',mos.moh())
print('masahat mosalas:',mos.mas())
q=int(input("enter qaede"))
e=int(input('enter your ertefa'))
py=pyramid(q,e)
print('masahat heram:',py.masa())