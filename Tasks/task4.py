#
# import time
#
# starting_point = time.time()
#
# while time.time() - starting_point < 10:
#     print("Its Loading")
#     time.sleep(1)
#
# print("Page is Loaded")
#
# """
# kas baige:
# Yra duotas listas, jame yra žodžiai. Parašyti algortimą, kuris atrinktų patį ilgiausią besikartojančių žodžių fragmenta. Pvz, jei listas:
# [‚namas‘, ‚namelis‘, ‚nameliukas‘] -> „nam“
# [morkytė, molas, morka] - > mo
# [namas, balkonas, mama] - > „“ tuscias stringas.
# """
# from itertools import combinations
#
#
# def longest_common_substring(words):
#     if not words:
#         return ""
#
#     first_word = words[0]
#     max_substring = ""
#
#     for i in range(len(first_word)):
#         for j in range(i + 1, len(first_word) + 1):
#             substring = first_word[i:j]
#             if all(substring in word for word in words[1:]):
#                 if len(substring) > len(max_substring):
#                     max_substring = substring
#
#     return max_substring
#
#
# # Test examples
# words_list1 = ["namas", "namelis", "nameliukas"]
# words_list2 = ["morkytė", "molas", "morka"]
# words_list3 = ["namas", "balkonas", "mama"]
#
# print(longest_common_substring(words_list1))  # "nam"
# print(longest_common_substring(words_list2))  # "mo"
# print(longest_common_substring(words_list3))  # ""

"""
Duotas listas skaiciu – [1, 2, 3, 4, 5, 6, 18, 90, 118, 991,  196151]. Grazinti dicta, kuris butu suskaiciuota kiek is siu skaiciu yra lyginiu, kiek nelyginiu: 

{ 

‚lyginiu_skaiciu_suma‘: suskaiciuotas kiekis‘, 

‚nelyginiu_skaiciu_suma‘: suskaiciuotas kiekis‘ 

}  
"""

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