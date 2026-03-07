import random
import string

class tcolors:
    GREEN = '\033[92m'
    NC = '/033[0m'

def generate_password():

    password_length = random.randint(10, 20)

    num_letters = random.randint(4, password_length - 4)
    remaining = password_length - num_letters
    num_numbers = random.randint(1, min(4, remaining - 1))
    num_symbols = remaining - num_numbers  # The rest are symbols

    letters = random.choices(string.ascii_letters, k=num_letters)
    numbers = random.choices(string.digits, k=num_numbers)
    symbols = random.choices("!@#$%^&*()-_=+", k=num_symbols)

    password_list = letters + numbers + symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


print("=== Password Generator ===\n")
print(f"Your secure password is: {tcolors.GREEN}{generate_password()}")
print('\n')
