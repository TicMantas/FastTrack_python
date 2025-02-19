def is_polindrome(n):
    return str(n) == str(n)[::-1]

for odometer in range(100000, 9999999):
    str_odometer = str(odometer)

    if not is_polindrome(str_odometer[-4:]):
        continue
    if not is_polindrome(str(odometer+1)[-5:]):
        continue
    if not is_polindrome(str(odometer +2)[1:5:]):
        continue
    if is_polindrome(str(odometer+3)):
        solution = odometer
        break

print(solution)