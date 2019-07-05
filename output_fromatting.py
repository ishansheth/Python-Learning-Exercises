'''
python geeksforgeeks example for the output formatting

'''

print("Geeks : %2d , portal: %5.2f"%(1,05.333))

print("Total students: %3d, boys: %2d"%(240,120))

print("%7.3o"%(25))

print("% 10.3E"%(356.08977))

print("I love {0} for {1} !".format('Geeks','Geeks'))

print("Number one portal is {0}, {1}, and {other}".format('Geeks','For',other='Geeks'))

print("Geeks : {0:2d}, portal : {1:8.2f}".format(12,00.546))

print("Second argument : {1:3d}, first one: {0:7.2f}".format(47.42,11))

print("Geeks: {a:5d}, portal: {p:8.2f}".format(a=453,p=59.058))

tab = {'geeks':4127,'for':4098,'geek':6876876}

print(" Geeks: {0[geeks]:d} for: {0[for]:d} Geeks: {0[geek]:d}".format(tab))

print(" Geeks: {geeks} for: {for} Geeks: {geek}".format(**tab))

class Person(object):

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return "{first} {last} is {age} years old".format(**self.__dict__)


p = Person('Ishan','Sheth',30)

print(p)

