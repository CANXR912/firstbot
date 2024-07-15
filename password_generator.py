import random
import string


def generate_password(pass_length):
    symbols = "+-/*!&$#?=@<>" + string.digits + string.ascii_letters
    password = ""
    for _ in range(pass_length):
        password += random.choice(symbols)

    return password
