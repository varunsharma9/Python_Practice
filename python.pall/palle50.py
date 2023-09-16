def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def generate_even_numbers(n):
    return [i for i in range(2, 2 * n + 1, 2)]

# Generate the first 1,000 prime numbers and even numbers
prime_numbers = generate_primes(1000)
even_numbers = generate_even_numbers(1000)

# Create a file and write the numbers to it in the specified format
with open("prime_and_even_numbers.txt", "w") as file:
    file.write("Prime numbers are below:\n")
    for prime in prime_numbers:
        file.write(f"{prime}\n")

    file.write("Even numbers are below:\n")
    for even in even_numbers:
        file.write(f"{even}\n")

print("Numbers have been written to 'prime_and_even_numbers.txt' file.")
