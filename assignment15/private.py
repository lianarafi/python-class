class password:
    def __init__(self):
        self.__password='lili15'
    def check_password(self,your_pass):
        if self.__password==your_pass:
            return True
        else:
            return False
p=password()
your_password=input('enter your password')
print(p.check_password(your_pass))
print(p.password)

    