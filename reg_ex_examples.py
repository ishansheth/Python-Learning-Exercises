'the package name re provides the full support of perl like expression to be matched in the text'
'the syntax is re.match(pattern, string, flags). This function returns a match object on success, None on failure.' \
'we use group(num) or groups() function to get the matched expression' \

import re
import csv
from collections import namedtuple


line = 'cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
    print('match.group():',matchObj.group())
    print('match.group():',matchObj.group(1))
    print('match.group():',matchObj.group(2))
else:
    print('No match')

'search function searches for first occurrence of RE pattern with string'

searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
if searchObj:
    print('search.group():',searchObj.group())
    print('search.group():',searchObj.group(1))
    print('search.group():',searchObj.group(2))
else:
    print('No match')


'Matching versus Searching'
'''python offers two different primitive operations based on regular expression. Match checks for a match only at the beginning 
of the string while search checks for a match anywhere in the string
'''

line_search = line

matchObj = re.match(r'dogs',line_search,re.M|re.I)

if matchObj:
    print('match.group():',matchObj.group())
else:
    print('No match')


searchObj = re.search(r'dogs',line_search,re.M|re.I)
if searchObj:
    print('search.group():',searchObj.group())
else:
    print('No match')


'search and replace'

phone_num = '2004-45-3433-2 # this is the phone number'

num = re.sub(r'#.*$','',phone_num)
print('phone num:',num)

print("Matched number in the phone_num line:",re.search(r'(\d+-?)+',phone_num).group())

print("Matched alphabets/words in the phone_num line:",re.search(r'([a-zA-z]+\s)+',phone_num).group())

print("Matched numbers in the phone_num line:",re.search(r'[^a-z#]+',phone_num).group())

'''Tokenizing Text'''

text = 'foo = 23 + 42 * 10'

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM =  r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES= r'(?P<TIMES>\*)'
EQ   = r'(?P<EQ>=)'
WS   = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))

# in this, ?P<TOKENNAME> convention is used to assign name to the pattern

scanner = master_pattern.scanner('foo=42');

#print(scanner.match())
a = 0
str = '32'
try:
    a = int(str)
except:
    print('cant be converted to integer')

'''generator example'''

def countdown(n):
    print("counting down!!")
    while n > 0:
        yield n
        n -= 1

c = countdown(5)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())


'''coroutines example'''

def print_matches(matchtext):
    print("Looking for",matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

def print_kwargs(**kwargs):
    print("keys of kwargs:",kwargs.keys())

matcher = print_matches('python')
matcher.__next__();
matcher.send('Hello')
matcher.send('python is cool')
a = [1,2,3,'ishan']
b = a
b[2] = 'sheth'
print(a)

a = {'name':'ACME', 'shares':105,'price':123.45}

print_kwargs(**a)
Stock = namedtuple('Stock_Apple',['name','shares','price','date','time'])
s = Stock('ACME',100,123.45,None,None)
s = s._replace(**a)
print(s)


with open('/home/ishan/ML_learning/review_data.csv','rt') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
