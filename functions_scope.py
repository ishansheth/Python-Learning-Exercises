
'''scoping rules in the functions in python'''

a = 42
b = 10
def foo():
    a = 30

foo()
print("a:",a)   # the value of a does not change here


def foo_1():
    global a    # 'a' is in global namespace now
    a = 30
    b = 20      # the value of b will not change as its not in the global namespace

foo_1()
print("a:",a)

# python supports nested functions definitions

def countdown(start):
    n = start
    def display():
        print("T-minus %d",n)
    def decreament():
        nonlocal n      # bind to outer n, only available in python 3
        global a
        a = 1000
        n -= 1
    while(n>0):
        display()
        decreament()

countdown(10)
print("a",a)


'''function as objects and closures'''