"""
- suskaiciuoti didziuju raidziu skaiciu +
- suskaiciuoti bendra raidziu skaciu +
- suskaiciuoti mazu raidziu skaiciu +
- suskaiciuoti lyginiu skaicu kvadratu suma +
- sudauginti nelyginius skaicius
- suskaiciuoti kitus simbolius
"""
worlds = """
London[c] is the capital and largest city[d] of both England and the United Kingdom, with a population of 8,866,180 in 2022.[2] Its wider metropolitan area is the largest in Western Europe, with a population of 14.9 million.[7] London stands on the River Thames in southeast England, at the head of a 50-mile (80 km) tidal estuary down to the North Sea, and has been a major settlement for nearly 2,000 years.[8] Its ancient core and financial centre, the City of London, was founded by the Romans as Londinium and has retained its medieval boundaries.[e][9] The City of Westminster, to the west of the City of London, has been the centuries-long host of the national government and parliament. London grew rapidly in the 19th century, becoming the world's largest city at the time. Since the 19th century,[10][11] the name "London" has referred to the metropolis around the City of London, historically split between the counties of Middlesex, Essex, Surrey, Kent, and Hertfordshire,[12] which since 1965 has largely comprised the administrative area of Greater London, governed by 33 local authorities and the Greater London Authority.[f][13]

As one of the world's major global cities,[14][15] London exerts a strong influence on world art, entertainment, fashion, commerce, finance, education, healthcare, media, science, technology, tourism, transport, and communications.[16][17] Despite a post-Brexit exodus of stock listings from the London Stock Exchange,[18][19] London remains a European economic powerhouse,[20] and one of the world's major financial centres. It hosts Europe's largest concentration of higher education institutions,[21] some of which are the highest-ranked academic institutions in the world: Imperial College London in natural and applied sciences, the London School of Economics in social sciences, and the comprehensive University College London.[22][23] It is the most visited city in Europe and has the world's busiest city airport system.[24] The London Underground is the world's oldest rapid transit system.[25]
"""

result = {
    "letters_number": 0,
    "upper_letters": 0,
    "lower_letter": 0,
    "odd_numbers": 1,
    "even_numbers": 0,
    "others_symbols": 0,
}

other_symbols = []

for symbol in worlds:
    if symbol.isdigit():
        symbol_integer = int(symbol)
        if symbol_integer % 2:
            result["odd_numbers"] *= symbol_integer
        else:
            result["even_numbers"] += symbol_integer ** 2
    elif symbol.isalpha():
        result["letters_number"] += 1
        if symbol.isupper():
            result["upper_letters"] += 1
        else:
            result["lower_letter"] += 1
    else:
        result["others_symbols"] += 1
        other_symbols.append(symbol)

print(result)