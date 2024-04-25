# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    
    
for i in range(11):
    print(i)

print(50*'-')

words = ['cat', 'window', 'defenestrate']

for i in range(len(words)):
    print(i,words[i], len(words[i]))

print(50*'-')

l = list(range(10))
print(l)

words = ['cat', 'window', 'defenestrate']

for i,w in enumerate(words):
    print(i,w)
    

to_find = 5
for i in range(10):
    print(i)
    if i ==15:
        pass
else:
    print("pas trouvé")


print(50*'-')
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.""" # DocString
    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n:int)->list:    
    """Return a Fibonacci series up to n.""" # DocString
    r = []
    a, b = 0, 1
    while a < n:
        r.append(a)
        a, b = b, a+b

    return r
    
    
r=fib2(12)

print(r) # [0,1,1,2,3,5,8]

print(fib2(12))


print(fib2)

print(50*'-')


def hello(name="GAURAT",firstName="NOFIRSTNAME",age=47):
    
    print("Hello "+name+" "+firstName)
    
hello()
hello("GAURAT","Fred")
hello(firstName="Fred",name="GAURAT")
# hello(firstName="Fred",name="GAURAT",47)
hello("GAURAT","Fred",age=47)


print(50*'-')

print(50*'-')

def oldadd(values:list)->int:
    r = 0
    for v in values:
        # r = v+r
        r+=v
    return r


def add(*values)->int:
    print(values)
    r = 0
    for v in values:
        # r = v+r
        r+=v
    return r

v = [10,20,30,40]
r = add(10,20,30,40)
print(r) # 100

r = add(*v)
print(r) # 100



print("toto",12,v)


def hello2(**data):
    print(data)
    print(data['firstName'],data['name'])
    # print("Hello "+name+" "+firstName)



hello2(firstName="Fred",name="GAURAT")


d = {'firstName': 'Fred', 'name': 'GAURAT'}
hello2(**d)




def the_function(value):
    print(value)
    
the_function("toto")
the_function(value="toto")

print(50*'-')


v = [10,20,30,40]


def mult2(values):
    r = []
    for v in values:
        r.append(v*2)

    return r


def mult2_item(value):
    return value*2

v = [10,20,30,40]

# the_result = mult2(v) 
# print(the_result) # [20,40,60,80]


# the_result = list(map(mult2_item,v))
the_result = list(map(lambda i:i*2,v))
the_lambda = lambda i:i*2
the_result = list(map(the_lambda,v))
print(the_result)

print(the_lambda(5))

