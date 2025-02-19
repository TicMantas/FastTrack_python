word = 'hello, {} {}!'
name = 'mantas'
surname = 'tickus'

print(f', {name} {surname}')
print('hello, {} {}'.format(name, surname))
print('hello, {1} {0}'.format(name, surname))
print(word.format(name, surname))

name = 'vardenis'
surname ='pavardenis'
print(word.format(name, surname))

# non pythonic
print('hello, ' + name + ' ' + surname)
