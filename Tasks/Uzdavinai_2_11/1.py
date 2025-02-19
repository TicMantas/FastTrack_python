import random
from random import randint


def divided_numbers(numbers, divisor):

    return [num for num in numbers if num % divisor == 0]

my_list = [random.randint(1,1001) for _ in range(10)]
divisor = 5
result = divided_numbers(my_list, divisor)


print(f'Random Number : {my_list}')
print(f'Numbers which can be divided from : {divisor}, result: {result}')



