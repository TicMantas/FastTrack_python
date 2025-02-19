#
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
#
# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 == num2:
#     print("num1 is equal to num2")
# else:
#     print("num2 is greater than num1")
# print('______________________________________________')
# # a = True
# #
# # if a==True:
# #     print("a is true")
# # else:
# #     print("a is false")
# #
#
# print('______________________________________________')

number = 15

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
