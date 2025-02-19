given_list = [1, 2, 3, 4, 5, 6, 18, 90, 118, 991, 196151]

result = {
    'even_numbers': 0,
    'odd_numbers': 0
}

for num in given_list:
    if num % 2 == 0:
        result['even_numbers'] += num
    else:
        result['odd_numbers'] += num

print(result)