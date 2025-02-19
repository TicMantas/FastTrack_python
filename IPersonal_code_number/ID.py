import datetime

def validate_personal_code(code):
    if not code.isdigit() or len(code) != 11:
        return False

    first_digit = int(code[0])
    if first_digit not in range(1, 7):
        return False

    year_prefix = {1: 1800, 2: 1800, 3: 1900, 4: 1900, 5: 2000, 6: 2000}
    year = year_prefix[first_digit] + int(code[1:3])
    month = int(code[3:5])
    day = int(code[5:7])

    try:
        datetime.date(year, month, day)
    except ValueError:
        print('data yra neteisinga')
        return False

    coefficients_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    coefficients_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    check_sum_1 = sum(int(code[i]) * coefficients_1[i] for i in range(10)) % 11
    check_digit = int(code[10])

    if check_sum_1 != 10:
        return check_sum_1 == check_digit

    check_sum_2 = sum(int(code[i]) * coefficients_2[i] for i in range(10)) % 11
    return (check_sum_2 if check_sum_2 != 10 else 0) == check_digit

code = input("Iveskite asmens koda: ")
if validate_personal_code(code):
    print("Asmens kodas yra teisingas.")
else:
    print("Asmens kodas yra neteisingas.")
