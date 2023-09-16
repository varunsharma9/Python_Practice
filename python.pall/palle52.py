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

def generate_even_numbers(n):
    return [i for i in range(0, n + 1, 2)]

# Generate prime numbers and even numbers in the range of 0 to 1000
prime_numbers = [num for num in range(0, 1001) if is_prime(num)]
even_numbers = generate_even_numbers(1000)

# Create a file and write the numbers to it in the specified format
with open("prime_and_even_numbers.txt", "w") as file:
    file.write("Prime numbers in the range 0 to 1000 are below:\n")
    for prime in prime_numbers:
        file.write(f"{prime}\n")

    file.write("Even numbers in the range 0 to 1000 are below:\n")
    for even in even_numbers:
        file.write(f"{even}\n")

print("Numbers have been written to 'prime_and_even_numbers.txt' file.")
