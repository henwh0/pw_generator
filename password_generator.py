import secrets
import string

class Colors:
    CYAN = '\033[0;36m'
    GREEN = '\033[0;32m'
    NC = '\033[0m'

def cprint(msg, Color=Colors.NC):
    print(f"{Color}{msg}{Colors.NC}")


def generate_pw():

    pw_length = secrets.choice(range(10, 21))
    num_letters = secrets.randbelow(pw_length - 4) + 4
    remaining = pw_length - num_letters
    num_numbers = secrets.randbelow(remaining + 1)
    num_symbols = remaining - num_numbers

    letters = [
        secrets.choice(string.ascii_letters)
        for _ in range(num_letters)
    ]

    numbers = [
        secrets.choice(string.digits)
        for _ in range(num_numbers)
    ]

    symbols = [
        secrets.choice("!@#$%^&*-_=+")
        for _ in range(num_symbols)
    ]

    password_list = letters + numbers + symbols
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)

cprint(f"\n=== Password_Generator ===", Colors.CYAN)
cprint(f"Your secure password is: {generate_pw()}\n", Colors.GREEN)
