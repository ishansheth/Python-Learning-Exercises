'''List compreshension'''

nums = [1,2,3,4,5]
squares = [n*n for n in nums]
print("list of square:",squares)

a = [-3,5,2,-10,7,8]
b = '''abs'''

e = [(x,y) for x in a for y in b if x > 0]
print(e)

'''Generator expression'''
'''It is same as list comprehension, but it iteratively produces the result'''

f_generator = (10*i for i in a)
print(f_generator.__next__())
print(f_generator.__next__())
print(f_generator.__next__())
print(f_generator.__next__())

'''eval, exec and compile'''
'''eval function executes an expression string and returns the result'''

e1 = eval("[(x,y) for x in a for y in b if x > 0]")

'''exec function executes a string containing arbitrary python code'''
exec('''print("after eval:",e1)''')

'''Both of these functions execute within the namespace of the caller   '''
