print("Hello' World")
print('Hello" World')

x, y = 5, 7

z= x+y
r=z+y
x=z
y=r


print('x: ', x)
print('y: ', y)

number = 2.0

print('variable :', number,type(number) )

variable = 'text'

print('variable', variable, type(variable))

variable = (1,)

print('variable', variable, type(variable))

my_list = [1,2,'mama',[1,2]]
print(my_list)

my_list = (1,2,'mama',[1,2])

print(my_list)


dict_type = {
    1: 'vienas',
    2: 'du',
    3: 'trys'
}

print(dict_type)

set_typ = {1,2,3}
frozen = frozenset(set_typ)
print(set_typ)

# bool
a= True
c= False
print(a,c)

bytes_type = b'Labas Vakaras Lietuva'
byte_array = bytearray(bytes_type)
print(bytes_type, type(bytes_type))

print(bytearray, type(byte_array))

