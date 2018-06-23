from collections import Counter
from operator import itemgetter
from operator import attrgetter
from datastruct import User
from collections import namedtuple
from collections import ChainMap

'calculation on the dictionary values'

price = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.22,
    'HPQ' : 37.50,
    'FB' : 10.75
}

# zip the prices and get the minimum of them
min_price = min(zip(price.values(),price.keys()))

print (min_price)

# sort the prices and get the minimum of them
sorted_price = sorted(zip(price.keys(),price.values()))

print (sorted_price)


print(min(price.keys())) # return the min key
print(min(price.values())) # return the min values, one has to get the corresponding key


print(min(price)) # return the min key, not values
print(max(price)) # return the max key, not values

print("key of min value is:",min(price,key=lambda k: price[k])) # this means, when price[k] is min, then return  that key.
# All the entries of dict will be passed iteratively, once we get the key, we can get the corresponding value of it

print("Min value is:",price[min(price,key=lambda k: price[k])])

# this function removes the duplicate entries from the list. The items in the list can be either hashable or non-hashable
def dedupe(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1,1,2,2,3,3,4,4,5,5,7]
x = list(dedupe(a))
print (x)

ab = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
# the below call creates the tuple of the values of dict and then checks if it exist in the seen set in dedupe function
# if the tuple exist in the set, then it will be eliminated, so in effect, elimination happens if both of the elements are unique
print(list(dedupe(ab,key=lambda d:(d['x'],d['y']))))

# if you want the elimination to happen on the key 'x' i.e. value of the single field in the dict, then, change lambda
print(list(dedupe(ab,key=lambda d:(d['x']))))

# this is how lambda works as shown below
func = lambda d:(d['x'],d['y'])
print(func({'x':1,'y':2}))


'count the occurance of every word in the list'

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3);
print("Top three occuraing words",top_three)

# one can also do it manually by iterating and putting them in a map
word_counts.clear()

for a in words:
    word_counts[a] += 1;
print("occurance of eyes",word_counts['eyes'])


morewords = ['why','are','you','not','looking','in','my','eyes']

# counter object also supports arithmatic operations
a = Counter(words)
b = Counter(morewords)
print(a,"\n",b)
c = a+b
print(c)

'sorting a list of dictionaries by a common key'

rows = [
    {'fname':'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname':'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname':'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname':'Big', 'lname': 'Jones', 'uid': 1004}
]

# this will sort the rows by the fname
'the sorted function takes callable object in keys argument. The itemgetter will create such a callable object'
'itemgetter function takes as argument the lookup indices which will be used to extract the desired values'

rows_by_fname = sorted(rows,key=itemgetter('fname'))
print("sorted the rows by fname",rows_by_fname)

# this will sort the rows by the uid
rows_by_uid = sorted(rows,key=itemgetter('uid'))
print("sorted the rows by uid",rows_by_uid)

# the above functianlity of the itemgetter can be replaced by the callable lambda as a keys argument

rows_by_fname_lambda = sorted(rows,key=lambda r:r['fname'])
rows_by_uid_lambda = sorted(rows,key=lambda r:r['uid'])
print("lambda to get and sort the items:",rows_by_fname_lambda)
print("lambda to get and sort the items:",rows_by_uid_lambda)

'sorting the objects without native comparison support'
lebara_users = [User(23),User(3),User(2)]
print("Sorted Lebara users:",sorted(lebara_users,key=lambda u:u.user_id))

# one can again use attrgetter to get the objects instead of lambda
print("Sorted Lebara users:",sorted(lebara_users,key=attrgetter('user_id')))
print("Lebara user with min id:",min(lebara_users,key=attrgetter('user_id')))
print("Lebara user with max id:",max(lebara_users,key=attrgetter('user_id')))

# getting all the first names
fname_list = [a.get('fname') for a in rows]
print("first names:",fname_list)

birthday_data = [
    {'address':'5412 N CLARK','date':'07/01/2012'},
    {'address':'5148 N CLARK','date':'07/04/2012'},
    {'address':'5800 N 58','date':'07/02/2012'},
    {'address':'2122 N ADDISON','date':'07/02/2012'}
]

'''
Extracting the subdirectory from the main directory
Supoose you want to make a directory which is a subset of another dictionary
This can be done usind dictionary compreshension
'''

# price dict is already defined above in the file, i am going to extract that here

p1 = {key:value for key,value in price.items() if value > 200}
print("sub dictionary:",p1)

tech_names = ['AAPL','IBM','HPQ','MSFT']
p2 = {key:value for key,value in price.items() if key in tech_names}
# p2 = {key:price[key] for key in price.keys() & tech_names}
print("sub dictionary:",p2)

# everything which is done above can be accomplished with creating a sequence of tuples and passing them to dict function
subdict_with_tuples = dict((key,value) for key,value in price.items() if value > 200)
print("sub directory created with tuples:",subdict_with_tuples)


'''Mapping names to sequence elements
Suppose you have a list or tuple and code that accesses the elements by their position. But this will reduce the
readability. collections.namedtuple() provide this benefits
'''

subscriber = namedtuple('Subscriber',['addr','joined'])

sub = subscriber('joneys@example.com','2012-10-19')

print(sub.addr,sub.joined)


'''
One another possible usecase of a namedtuple is that they can replace dict. So if you are building large data structure with
dictionary, namedtuple will be more efficient. But namedtuple is unmutable unlike dict
'''

Stock = namedtuple('Stock',['name','shares','price','date','time'])

s = Stock('ACME',100,123.45,None,None)
#s.shares = 20  --> Exception

'if you want to change any of the attributes, then it can be done using replace method'

s = s._replace(shares=75)
print(s)

'the subtle use of replace method is that, you can create the prototype with default values and then use replace method'

stock_proto = Stock('',0,0.0,None,None)
def dict_to_stock(s):
    return stock_proto._replace(**s)
a = {'name':'ACME', 'shares':100,'price':123.45}
print("from dict to namedtuple:",dict_to_stock(a))
b = {'name':'ACME', 'shares':100,'price':123.45, 'date':'12/17/2012'}
print("from dict to namedtuple:",dict_to_stock(b))


'''
chainmap: suppose that you have a multiple dict and you have to lookup each of them if certain items are not found in one after 
the other, then you can use chainmap
'''
c = ChainMap(a,b)
print("length of chainmap",len(c),"\n key and values",list(c.keys()),list(c.values()))

'if there are multiple keys then values from the first mappings get used. Operations that mutate the mapping always affect the ' \
'first mapping listed'

'Alternative to the chainmap, you might consider merging dict using update() method'
dict_a = {'x':1,'z':3}
dict_b = {'y':2,'z':4}

merged_dict = dict(dict_b)
merged_dict.update(dict_a)
print("merged dictionary:",merged_dict)

# this required you to completely make separate dictionary object. Therefore, if any of the original dict changes, that will
# not be reflected in the new merged dict. ChainMap uses original dict, thats why it does not have this behaviour