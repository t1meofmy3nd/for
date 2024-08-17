numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

is_prime = True
count = 0

for a in range(numbers[1], numbers[-1] + 1):
    for b in range(2, a):
        result = a % b
        if result != 0:
            is_prime = True
        else:
            is_prime = False
            break
    if is_prime:
        primes.append(a)
    else:
        not_primes.append(a)

print(f"primes:{primes}")
print(f"not_primes:{not_primes}")
