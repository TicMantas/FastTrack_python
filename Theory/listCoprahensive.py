result = []

for number in range (21):
    if number % 2 == 0:
        result.append(number * 2)
print(result)

result = [value * 2 for value in range(21) if value % 2 ==0]
print(result)