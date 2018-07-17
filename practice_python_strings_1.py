'''suppose you want to split the string into fields and then put them into the list. But the delimiters are not consistent
The split method is used for simple cases and can not be used for this complicated processing. In this case use re
'''

import re

line = "asds dfdfd: fdsfs,     foo"
string_fields = re.split(r'[;,:\s]\s*',line)
'''the delimiter will be comma, semicolon, whitespace followed by any amount of extra whitespace'''
print("splitted string:",string_fields)

'''if there is a cpature group in the text, then it also becomes the part of result. So one needs to be careful when using the re'''

fields = re.split(r'(;|,|:|\s)\s*',line)
print("splitted string using capture group",fields)
print(fields[::2])
print('Delimiters',fields[1::2]+[''])
'''combine delimiters and fields togather'''
original_string = ''.join(v+d for v,d in zip(fields[::2],fields[1::2]+['']))
print(original_string)


'''Matching and searching for text patterns'''
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))


'For more complicated matching, use re module'
text1 = '11/27/2012'
text2 = 'Nov,27 2012'

if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

date_pattern = re.compile(r'\d+/\d+/\d+')

if date_pattern.match(text1):
    print('yes')
else:
    print('no')

if date_pattern.match(text2):
    print('yes')
else:
    print('no')

# match function tries to find only the matching pattern at the start of the string and if you want to search
# for all occurences of a pattern, use findall() method instead.

text = 'Today is 11/27/2012. Pycon starts 3/13/2013'
print("all matched patterns in the text:",date_pattern.findall(text))

'when defining regular expression, it is common to introduce capture groups by enclosing parts of pattern in parentheses'
date_pattern_group = re.compile(r'(\d+)/(\d+)/(\d+)')
m = date_pattern_group.match('11/27/2017')
print("group 0:",m.group(0))
print("group 1:",m.group(1))
print("group 2:",m.group(2))
print("group 3:",m.group(3))
print("all groups :",m.groups())
print("matched all pattern groups in text",date_pattern_group.findall(text))

'findall finds all the matches and returns them as a list. But if you want them iteratively, then use finditer() method'

for m in date_pattern_group.finditer(text):
    print("Printing group iteratively:",m.groups())

print(date_pattern_group.match('11/27/2012asdasdas').group(0))

# searching and replacing the text pattern in a string

text_replace = "yeah but yes yuppp and yo , i am not sitting in my room and focusing on learning pythong throughly"
print(text_replace.replace('yeah','yep'))

'''suppose you want to do more complicated things and for that use sub() method in 're' module. E.g. there are dates in 11/27/2012
and you want to write them as 2012-27-11
'''

print("Replaced text:",re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
print("Replaced text with pre-compiled pattern:",date_pattern_group.sub(r'\3-\1-\2',text))

'''string formatting using formatter string'''

stock = {'name':'GOOG','shares':100,'price':490.10}
r = "{0[name]} {0[shares]} {0[price]}".format(stock)
print("formatted string:",r)

x = 3 + 4j;
complex_num = "{0.real} {0.imag}".format(x)
print("complex number",complex_num)

formatted_string = "{name:8} {shares:8d} {price:8.2f}".format(name='IBM',shares=1033,price=123.4567)
print("formatted strings",formatted_string)


