import math
class circle:
    def __init__(self,sh,):
        self.radius=sh
    def masahat(self):
        return(self.radius*self.radius*math.pi)
    def mohit(self):
        return(self.radius*math.pi*2)
class Sphere(circle):
    def hajm(self):
        return(self.radius**3*math.pi*(4/3))
    def mashat(self):
        return(self.radius**2*math.pi*4)
sh=float(input('enter your radius'))
rec1=circle(sh)
print('mashat dayere:',rec1.masahat())
print('mohit dayere:',rec1.mohit())
cir=Sphere(sh)
print('hajm kore:',cir.hajm())
print('masahat kore',cir.mashat())

