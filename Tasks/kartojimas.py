def function_1 ():
    print(1)
    return 1
def function_2 ():
    print(2)
    return 2
def function_3 ():
    print(3)
    return 3
def function_4 ():
    print(4)
    return 4
def function_5 ():
    print(5)
    return 5





functions = {
    1: function_1,
    2: function_2,
    3: function_3,
    4: function_4,
    5: function_5,
}
result = functions[4]
print(result)