# new_set = {1,2,4,3,4,5}
# print(new_set)
# new_set = {1,2,4,3,4,5,'a','c', 'b'}
# fr = frozenset(new_set)
# print(new_set)
# new_set.add(6)
# print(new_set)
# new_set.add('d')
# print(new_set)
#
# my_list = [1,2,3,4,5,5,6,6,7,7]
# print(set(my_list))
#
# print('___________________________________________')


data = [(1, 8, 'naujas'), 'begemotas', 123456789, [1, 2, 'masina']]

jas = data[0][2][-3:]
gem = data[1][2:5]
num = str(data[2])[3:6]
an = data[3][2][-1:-3:-1]



print(jas)
print(gem)
print(num)
print(an)