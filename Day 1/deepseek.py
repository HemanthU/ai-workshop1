def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check for factors from 3 to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    """Print all prime numbers between start and end (inclusive)."""
    print(f"Prime numbers between {start} and {end}:")
    primes_found = []
    
    for num in range(start, end + 1):
        if is_prime(num):
            primes_found.append(num)
            print(num, end=" ")
    
    if not primes_found:
        print("No prime numbers found in this range.")
    else:
        print(f"\n\nTotal primes found: {len(primes_found)}")

# Example usage
print_primes(1, 100)