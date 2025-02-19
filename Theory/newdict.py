new_dict = {
    "a": 1,
    0: (1, 2, 3, 4),
}

print(new_dict)

new_dict['3'] = 3
print(new_dict)

del new_dict['3']
print(new_dict)

new_dict[0] = (1, 0)
print(new_dict)

value = new_dict.get(5, False)

print('value', value)
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())
print('------------------------------------------------')
data = (1, 2, 3, 4)

a, b, *c = data

print(a, b)
print(c)