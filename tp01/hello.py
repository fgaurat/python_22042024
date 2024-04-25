

# the_world_is_flat : snake_case
# TheWorldIsFlat : UpperCamelCase
# theWorldIsFlat : camelCase
# the-world-is-flat : kebab-case

print("Hello")

the_world_is_flat = False
a=2

print(type(the_world_is_flat))
print(type(a))


if the_world_is_flat:
    print("Be careful not to fall off!")

s = "toto"
s2 = 'toto'

# print(n)

s = 'L\'orage gronde.'
print(s)
s = "L'orage gronde."
print(s)

p = "c:\\truc\\normal"
p = r"c:\truc\normal"
print(p)

m = """une ligne 
une ligne 
une ligne 
une ligne 
une ligne 
"""
print(m)

s1 = "10"
s2 = "tutu"
s3 = s1+s2
print(s3)
i = 10
s3 = int(s1)+i

print(s3)

print(s2*i)
print(20*"-")

s = "Python"
print(s[0])
# s[0] = 'J'
# print(s[0])


a = 2
print(hex(id(a)))
a = 3
b = 3
print(hex(id(a)))
print(hex(id(b)))
a=14
s = "Python"

print(len(s))

l = s[-6]
print(l)

s = "Python"

print(s[2:4])# characters from position 2 (included) to 4 (excluded)
print(s[2:5])# characters from position 2 (included) to 5 (excluded)
print(s[2:])# characters from position 2 (included) to the end
print(s[:5])# characters from start (included) to 5 (excluded)
print(s[:])# all

print(s[15:87])

j = 'J'+s[1:]
print(j)

print(50*'-')
squares = [1, 4, 9, 16, 25]
print(type(squares))
print(squares)
print(squares[-1])
squares[0] =1000
print(squares)
l = [12,89,786,65]
print(squares+l)
squares.append(36)
print(squares)

print(50*'-')
squares = [1, 4, 9, 16, 25]
squares2 = squares[:]
squares[0]=1000
print(squares)
print(squares2)

l1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

import copy
print(l1[1][1])
# l2 = l1[:]
l2 = copy.deepcopy(l1)
l1[1][1] = 1000
print(l1)
print(l2)
print(50*'-')

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b





