"""
Yra stringas; ‚1asdg16asdg1wg16ewrg1er6gw1‘.
Suskaiciuoti ir grazinti dicte kiek yra skaiciu ir kiek yra raidziu.
"""

result = {
    'letters':0,
    'numbers':0
}
string = "1asdg16asdg1wg16ewrg1er6gw1"

for symbol in string :
    if symbol.isdigit():
        result['numbers'] += 1
    else:
        result['letters'] += 1
print(result)
