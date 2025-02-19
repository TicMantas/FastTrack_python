from cow_bulls.cow_bull import generate_field, check_bull_number, check_cows_number

def main():
    field= generate_field()
    player_prediction = int(input('Ivesk spejimu skaiciu'))
    print(field)
    print(player_prediction)