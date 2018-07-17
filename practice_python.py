from datastruct import *
from collections import defaultdict
from collections import OrderedDict
import json

'unpacking the values from list'

data = ['ACME',50,91.1,(2012,12,21)];
name,shares,price,date = data;

print('unpacking the values from list')
print(name)
print(date)

'unpacking the values from list---------end'



'unpacking multiple values from the list in a single variable'

print('unpacking multiple values from the list in a single variable')

*trailing,current = [10,8,4,5,6,7,8,9]
print(current)

record = ('Dave','dave@example.com','777-888-345','345-432-567')
name,email,*phone_numbers = record

print(phone_numbers)

records = [('foo',1,2),('bar','hello'),('foo',3,4)]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)



#if __name__ == '__main__': # execute only if the file name is 'main'

line = 'nobody:*:-2:-2:unprivileged user:/var/empty:/usr/bin/false'

uname,*fields,homedir,sh = line.split(':')
print(fields,sh)

'unpacking multiple values from the list in a single variable----------------end'

nums = [1,2,3,4,5,6,7,8,6,5,4,4,5,56,6];

print(heapq.nlargest(3,nums)) # prints 3 largest numbers from nums
print(heapq.nsmallest(3,nums)) # prints 3 smalles numbers from nums


'priority queue in the python'
#importing the class from datastruc.py


print('priority queue in the python')

q = PriorityQueue()

q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

'priority queue in the python-------------end'



'mapping keys to multiple values'

print('mapping keys to multiple values')

def_d = defaultdict(list)
def_d['a'].append(1);   # creates the key and value even if key does not exist. If key does not exist, it will be created
def_d['a'].append(2);
def_d['a'].append(3);
def_d['a'].append(1);
print(def_d['a'])


def_d_set = defaultdict(set)
def_d_set['a'].add(1);
def_d_set['a'].add(2);
def_d_set['a'].add(3);
def_d_set['a'].add(1);
print(def_d_set['a'])

'mapping keys to multiple values-------------------------end'

'keeping an order in the dictionary'

print('keeping an order in the dictionary')

# ordered dictionary is twice as large as normal dictionary, so one must be careful while using it in an application
ordered_d = OrderedDict();
ordered_d['foo'] = 1
ordered_d['bar'] = 2
ordered_d['spam'] = 3
for key in ordered_d:
    print(key,ordered_d[key])

#  dict_to_json is a string object, so ordered dict are very useful in json parsing or creation

dict_to_json =json.dumps(ordered_d)
print((dict_to_json))

'keeping an order in the dictionary-------------------------------------end'





