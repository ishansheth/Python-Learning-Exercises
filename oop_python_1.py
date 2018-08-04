import random

class Account(object):
    num_accounts = 0    # this is not tied to any of the object and its value is shared among all the objects/instances of the class

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self,amt):  # instance methods
        self.balance += amt     # classes do not create the scope for the names used inside the bodies of methods. #
        # Therefore, always use self.balance and not balance

    def withdraw(self,amt):     # instance methods
        balance = 100
        self.balance -= amt

    def inquiry(self):      # instance methods
        return self.balance


class Foo(object):
    def bar(self):
        print("Bar!!")

    def spam(self):
        self.bar()  # do not use bar() or bar(self) but self.bar() otherwise it will give NameError
        Foo.bar(self)   # this works also fine


'''Inheritance: Super class of EvilAccount is Account. Inheritance below is implemented with only slight enhancement of the dot operator
Specifically, if the search for an attribute does not find a match, then search moves on to the base class'''
class EvilAccount(Account):
    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * 1.10
        else:
            return self.balance

#create a few accounts
a = Account('Billy',10)     # invokes Account.__init__(a,'Billy',10)
b = Account('Bill',100)

a.deposit(100)
b.withdraw(50)
print(a.name)

'''explicit use of self is required because python does not provide a means to explicity declare a variable like C and C++. Without this there is no way to know
whether an to a variable in a method is supposed to be a local varible or if its supposed to be saved as an instance attribute. The explicit use of self fixes
this - all values stored on self are part of the instance and all other assignments are just local variables '''


c = EvilAccount("George",100)
c.deposit(10)   # this calla the method deposit() defined in the Account class
print(c.inquiry())

'''A subclass can also have __init__() method and add its own new attributes'''
'''sometime you want to call the method of the super class which has original implementation, for that, super().<MethodName>() can be used'''
class MoreEvilAccount(EvilAccount):
    def deposit(self,amount):
        self.withdraw(5)    # subtract convenience fee
        super().deposit(amount)


ex = MoreEvilAccount("heyo",100)
ex.deposit(1)
print(ex.inquiry())


