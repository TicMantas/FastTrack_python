
import random
def generate_random():
    generated_number = ''
    while len(generated_number)<4:
        current_number = str(random.randint(0,9))
        if not current_number in generated_number:
            generated_number += current_number
    return generated_number

guess_amount = int(input('Enter How many guess you need : '))
generated_number = generate_random()
print(generated_number)

while guess_amount > 0:
    current_guess = int(input('Enter Your Guess : '))
    current_guesses = str(current_guess)
    bulls=0
    cows=0

    for i in range (len(generated_number)):
        if current_guesses[i] in generated_number[i]:
            if current_guesses[i] == generated_number[i]:
                bulls+=1
            else:
                cows+=1
    print(f'Cows: {cows}, Bulls : {bulls}')

    if not bulls < 4:
        print (f'You win ! You still had : {guess_amount} guesses')
        break

    guess_amount-=1

    if not guess_amount > 0:
        print(f'you Lose ! the answer was : {generated_number}')





