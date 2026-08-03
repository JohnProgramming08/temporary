from random import choice
import requests


# Return whether or not a given number is prime
def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False

    end = int(n**0.5) + 1
    for i in range(3, end, 2):
        if n % i == 0:
            return False

    return n != 1


# Output the first n terms of the fibbonacci sequence
def fib_sequence(n: int) -> None:
    current_term = 1
    previous_term = 0
    for i in range(n):
        print(current_term)
        temp = current_term
        current_term += previous_term
        previous_term = temp


# Return a random word
def random_word() -> str:
    words = [
        "Sigma",
        "Dope",
        "Labour",
        "Greens",
        "Tory",
        "Reform",
        "Restore",
        "Mayor",
    ]
    return choice(words)


# Return a string with the first letters of each word in a given string
def first_letters(strng: str) -> str:
    strng = strng.split(" ")
    return "".join([word[0] for word in strng])


# Return a list of pairs of factors of a given number
def get_factor_pairs(num: int) -> list:
    res = []
    target = int(num**0.5) + 1
    for i in range(1, target):
        if num % i == 0:
            res.append((i, num // i))

    return res


# Return if a given number is a square number
def is_square(num: int) -> bool:
    return (num**0.5) % 1 == 0


# Count the frequency of each character in a given string
def count_character_frequency(strng: str) -> dict:
    count_dict = {}
    for char in strng.lower():
        letter_count = count_dict.get(char, 0)
        count_dict[char] = letter_count + 1

    return count_dict


print(count_character_frequency("Dylan Scully is the sigmaj"))
requests.get("https://labour.org.uk")
