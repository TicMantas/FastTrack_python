
"""
mutable:
list

immutable:
str, int, float, tuple, range, bytes, bytearray, set, frozenset
"""

my_list = []
print(my_list, type(my_list))
print(len(my_list))

my_list = [1, 2, 3]
print(my_list, type(my_list))
print(len(my_list))

i: int
for i in my_list:
    print(i, i+5)
print('________________________________________')
c= 8
my_list.append(c)
print(my_list)
c=[1,2,3]
my_list.append(c)
print(my_list)

print('Pop :' ,my_list.pop())
print(my_list)

my_list.remove(1)
print(my_list)


my_list = [1, 2, 3]
b =10
my_list.append(b)
print(b)
print(my_list)

b=18
print(b)
print(my_list)#  mutable / immutable

print('________________________________________')

text = 'abc'

print(text.replace('a', 'A'))
print(text)
my_list = [1, 2, 3]
print(my_list.append(10))
print(my_list)

a = [1, 2, 3]
print(a)
b = a
print(b)


a.append(5)
print(a, id(a))
print(b, id(b))

print('________________________________________')

# len
number = 123456
print(len(str(number)))

print('________________________________________')

my_list = [1, 2, 3,4,5,6,7,8]

print(my_list[:4])

print('________________________________________')

my_list = [1, 2, 3, 4, 'mama']
address = id(my_list)
my_list[4]= my_list[4].capitalize()



print(my_list)


print(id(my_list) == address)

print('________________________________________')

my_list = [1, 2, 3, 2,]

print(sum(my_list))
print(min(my_list))
print(max(my_list))

if 1 in my_list:
    print('Yra toks skaicius')
else:
    print('Tokio skaiciaus nera')

my_list.sort()
print(my_list)
# nepakeicia listo tiesiog isprintina
print(sorted(my_list))
print(sorted(my_list, reverse=True))
print('________________________________________')
my_list.sort(reverse=True)
print(my_list)
print('________________________________________')
naujas_list = my_list.copy()
new_list = list(my_list)
print('________________________________________')
my_list += ['abc', 'abc']
new = my_list + ['abc', 'abc']
print(my_list)
print(new)
print('________________________________________')

my_list = ['objektas1', 'objektas2', 12315125125, 1245125125]

print(my_list[2:4])