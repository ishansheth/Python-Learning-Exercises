import sys
from math import *
from random import randrange
import re


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

tab1 = {'geeks':4127,'for':4098,'geek':6876876}

tab2 = {'leetcode':41,'hackerrank':40,'codechef':68}

print(" Geeks: {0[geeks]:d} for: {0[for]:d} Geeks: {0[geek]:d}, programming portal : {1[leetcode]:d}".format(tab1,tab2))

print(" Geeks: {geeks} for: {for} Geeks: {geek}".format(**tab1))

class Person(object):
    val = 100
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return "{first} {last} is {age} years old".format(**self.__dict__)


p = Person('Ishan','Sheth',30)


nameList = ['Harsh','Pratik','Bob','Dhruv']
pos = 0
try:
    pos = nameList.index('Bob')
    print(nameList[:])
except:
    print("Bob1 is not preset in the list")


list1 = ['physics','chemistry',1997,2002]
list2 = [1,2,3,4,5,6,7]

#printing the list in reversed order
for i in list1[::-1]:
    print(i)

temp = 'Geeks 22564 for 445 geeks'
data = [x for x in (int(x) for x in temp if x.isdigit()) if x%2 == 0]
print(data)

L1 = [1,2,3,4,5]
#shallow copy
L2 = L1

#deep copy
L3 = L1.copy()

#deep copy
L4 = list(L1)

L1[0] = [5]

print(L1,L2,L3,L4)


# empty tuple requires 48 bytes and then every elements needs 8 more bytes
T1 = tuple()
print(sys.getsizeof(T1))

T1 = (1,2)
print(sys.getsizeof(T1))

T1 = (1,3,(4,5))
print(sys.getsizeof(T1))


L1 = [1,1.33,'GFG',0,'No',None,'G',True]
val1,val2 = 0,''
for i in L1:
    if(type(i) == int or type(i) == float):
        val1 += i
    elif(type(i) == str):
        val2 += i
    else:
        break

print(val1,val2)

L1 = [x**2 for x in range(10)].pop()
L1 += 19
print(sqrt(L1),end=" ")

L1 = [x**2 for x in reversed(range(10))].pop()
L1 += 16
print(int(sqrt(L1)))


D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]

print(D)

D = {1:[1,2,3],2:(4,6,8)}
D[1].append(4)

print(D[1],end=" ")
L = list(D[2])
L.append(10)

D[2] = tuple(L)
print(D[2])

a = 2.13
b = 3.777
c = -3.12

print(int(a),floor(b),ceil(c),fabs(c))

p = re.compile('\d+')
print(p.findall("I met him once at 11 AM on 4th of July 1887"),end=" ")
p = re.compile('\d')
print(p.findall("I met him once at 11 "))

print(re.sub('ge','**','Geeksforgeeks',flags=re.IGNORECASE), end=" ")
print(re.sub('ge','**','Geeksforgeeks'))


