




for e in range (0, 10):
    if e == 8:
        break
    if e % 2:
        continue
    print(e)
else:
    print('praejo')

values = 'aofgsongoasfsdhgs'
values = [1,2,3,4]
values = (1,2,3,4)
values = {1,2,3,4}
values = {
    1: 'vienas',
    2: 'du',
    3: 'trys'
}

for key, value in values.items():
    print(key, value)

number = 10
for i in range(2, number):
    print(i)