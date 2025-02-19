def reverse_int(n):
    numbers = ' '.join(str(n)[::-1])
    return numbers

number = int(input('Enter integer : '))
print(reverse_int(number))