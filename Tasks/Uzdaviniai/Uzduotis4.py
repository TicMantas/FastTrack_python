def process_data(data):
    result = {}

    for item in data:
        if isinstance(item, int):
            result[item] = item ** 2
        elif isinstance(item, str):
            result[item] = len(item)
        elif isinstance(item, list):
            result[tuple(item)] = sum(item)
        elif isinstance(item, dict):
            result[str(item)] = sum(item.values())
        elif isinstance(item, tuple):
            product = 1
            for num in item:
                product *= num
            result[item] = product
    return result

data = [3, 2, 'm', 'lele', (1, 2, 3), [1, 2, 3], {'vienas': 1, 'du': 2}]

processed_data = process_data(data)

print(processed_data)