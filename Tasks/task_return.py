def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True

def check_prime_list(numbers):
    prime_numbers = [number for number in numbers if is_prime(number)]
    non_prime_numbers = [number for number in numbers if not is_prime(number)]
    return prime_numbers, non_prime_numbers

numbers_list = [int(number) for number in input('Enter a number speperated with spaces : ').split()]

primes, non_primes = check_prime_list(numbers_list)
print(f"Prime numbers: {primes}")
print(f"Non-prime numbers: {non_primes}")