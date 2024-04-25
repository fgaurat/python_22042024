

l = [10,20,30]
print(l)
l.append(40)
print(l)
r = l.pop()
print("last value",r)
print(l)
l.insert(0, 0)
l.insert(0, -10)
print(l)
f = l.pop(0)
print("first value",f)
print(l)

from collections import deque

d = deque(l)
print(d)
d.appendleft(-10)
print(d)

print(50*'-')

l=[]
for i in range(10):
    l.append(i)

print(l)

l= list(map(lambda i:i,range(10)))
print(l)

l=[i for i in range(10)] # List Comprehensions


dirty_data = [
    "  fdfsd", 
    "fdsf    ",
    "    fdsf    ",
]

clean_data = [d.strip() for d in dirty_data]
print(clean_data)



print(50*'-')

t = (0,1,2)

print(t[0])
# t[0] = 1000
# print(t[0])


a,b,c,*d = (0,1,2,3,4,5,6)

print(a,b,c,d)

def f():
    return 12,5

a,b = f()
print(a)

# a,b,c,d,e = 0,1,2


# sets

s = {2,2,5,5,9,7,5,6,2,9}
l = [2,2,5,5,9,7,5,6,2,9]
l1 = list(set(l))
print(s)
print(l1)



the_data = {
    "name":"GAURAT",
    "firstName":"Fred",
    "age":47,
    "languages":[
        "Python",
        "PHP"
    ]    
}


print(the_data['name'])
print(the_data['languages'])
the_data['name'] = "DURAND"

for k in the_data:
    print(k,the_data[k])
    
for k,v in the_data.items():
    print(k,v)
    

print("toto" in the_data.keys())



