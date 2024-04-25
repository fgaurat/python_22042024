
b = 10

def the_function():
    global b    
    b=12
    print(b)
    if True:
        a = 0
    print(a)

the_function()

print(b)
