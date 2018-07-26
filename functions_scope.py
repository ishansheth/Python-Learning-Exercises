
'''scoping rules in the functions in python'''
import foo as methods

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
x = 4321

def helloworld():
    return "hello world, val of x:%d" % x

'''n the above case, the helloworld function uses the value of x that is defined in the same environment as where helloworld
function is defined. Although variable 'x' with same name is define in the module where this function is being called, #
that is not used. When the statements that make up a functions are packaged together with the environment in which they execute, the 
resulting object is known as closure 
'''

print(methods.callf(helloworld))
print(helloworld.__globals__)   # in this one can see the

'''when nested functions are used, closure capture the entire environment needed for the inner function to execute'''

def bar():
    x = 13;
    def helloworld():
        return "hello world, val of x:%d" % x

    print(methods.callf(helloworld))

bar()

'''closure is highly effective way to  preserve state across a series of function calls'''
def countdown_1(start):
    def next():
        nonlocal start
        r = start
        start -= 1
        return r
    return next


next = countdown_1(10)
while True:
    v = next()
    print(v)
    if not v: break

