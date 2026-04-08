# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check till sqrt(n)
        if n % i == 0:
            return False
    return True

# Function to print prime numbers up to a limit
def print_primes(limit):
    print("Prime numbers up to", limit, "are:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")

# Main program
limit = int(input("Enter the limit: "))
print_primes(limit)