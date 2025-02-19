from Tasks.import_tasks.list import my_list

print(my_list)

def calculate_number(numbers):
    results= dict(odd=1, even=0)

    for number in numbers:
        if not type(number) is int:
            continue
        if number % 2==0:
            results['even'] += number
        else:
            results['odd'] *= number
    return results

result = calculate_number(my_list)

print(result)
