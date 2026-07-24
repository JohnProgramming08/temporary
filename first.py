print("All even numbers between 2 and 100 inclusive.")
for i in range(2, 101, 2):
    print(i)


# Return whether or not a given number is prime
def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False

    end = int(n**0.5) + 1
    for i in range(3, end, 2):
        if n % i == 0:
            return False

    return n != 1
