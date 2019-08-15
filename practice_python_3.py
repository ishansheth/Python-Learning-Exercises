'''
python questions from geeksforgeeks
https://www.geeksforgeeks.org/output-python-program-set-1/
'''

import sys
from math import sqrt

r = lambda q: q*2
s = lambda q: q*3
x = 2

x = r(x)
x = s(x)
x = r(x)
print(x)

a = 4.5
b = 2

# truncated division 
print(a//b)

count = 1

def doThis():
    global count

    for i in (1,2,3):
        count += 1

doThis()

print(count)


def foo(bar,lee):
    print(bar,lee)

ll = [1,2]
foo(*ll)

def bar(**kwargs):
    for a in kwargs:
        print(a,kwargs[a])

fam = {"ishan":30,"het":21,"papa":60,"mummy":56}

bar(**fam)

def gfgFunction():
    "GeeksForGeeks is a cool website to boost the technical skills"
    return 1


print(gfgFunction.__doc__)

check1 = ["Learn","Quiz","Practice","Contribute"]
#shallow copy
check2 = check1

# deep copy
check3 = check1[:]

# this statement will change check2 and also check1 list value
check2[0] = "Code"

# this will only change check3
check3[1] = "Mcq"

for c in (check1,check2,check3):
    print(c)


def gfg(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

gfg(2)
gfg(3,[3,2,1])

list1 = [2,4,6,8]
print([i*i for i in list1])
print(list1.index(8))
print("C:\\inside C directory")
print(r"C:\\inside C directory")
print("\x25\x26")

data = 50

# when exception occurs, the except block will be executed
# when there is no exception then else block will be executed

# when else and finally both are present-> if exception, then except and finally
#                                       -> if no exception, then else and finally

try:
    data = data/0
except ZeroDivisionError:
    print("Can not divide by 0")
else:
    print("Division successful")
    
try:
    data = data/5
except:
    print("Inside except block")
else:
    print("GFG division by 5 successful")

try:
    data = data/10
except:
    print("Inside except block, division by 0 is not possible")
else:
    print("else GFG")
finally:
    print("finally Geeksforgeeks")



List = [True,50,10]
List.insert(2,5)

print(List,"Sum is:",sum(List))

# remove removes the first matching value, not a specific index, throws ValueError exception
# del removes the item at a specific index, throws IndexError exception
# pop removes the item at specific index and returns it, throws IndexError exception

L = [1,3,5,7,9]
print(L.pop(-3))
print(L.remove(L[0]))
print(L)


L1 = [x**2 for x in range(10)].pop()
L1 += 20
print(sqrt(L1))
# converting to int
print(int(sqrt(L1)))

L1 = [x**2 for x in reversed(range(10))].pop()
L1 += 16
print(sqrt(L1))



#---------------------Type Conversion----------------------------------


s = "10010"
c = int(s,2)
print("After converting binary string to integer base 2:",c)

e = float(s)
print("After converting binary string to float:",e)

s="a"
print("After converitng character to integer:",ord(s))

c = hex(56)
print("After converitng integer to its hex val:",c)

c = oct(56)
print("After converitng integer to its oct val:",c)


s = "geeks"
print("After converting string to tuple:",tuple(s))

print("After converting string to set:",set(s))

print("After converting string to set:",list(s))

a = 1
b = 2

tup = [['a',1],['b',2],['c',3]]

c = complex(1,2)
print("After convering integers to complex:",c)

c = str(a)
print("After convering integers to string:",c)

# in this case, it can be also tuple of tuples as well as list of lists
c = dict(tup)
print("After convering list to dict:",c)

