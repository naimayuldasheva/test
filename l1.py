class Subscriber:

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return self.firstname + self.lastname

class Provite():

    def __init__(self,name):
        self.name = name
        self.subscribers = ['mna','krmv'] 
        self.payments = {}

    def register_payment(self,Subscriber,number):
        if Subscriber in self.subscribers:
            self.payments[Subscriber]= number
            return True
        else:
            raise ValueError

class Terminal:

    anout = 0
    providers = []
    def register(self,prov):
        self.providers.append(prov)

    def pay(self, prov, sub, num):
        self.providers = num
        result = prov.register_payment(sub,num)
        if result is True:
            self.providers+= num

sub = Subscriber('mna' ,'krmv')
provide = Provite('Admin')
ter = Terminal()
ter.register(provide)
ter.pay(provide, sub.firstname, 1000)
print(ter.providers, ter.providers)
print(provide.payments)









