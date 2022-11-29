from random import sample
import string


def get_random_password(size=8) -> str:
    alphabet = string.ascii_uppercase + string.digits + string.ascii_lowercase
    password = "".join(sample(alphabet, size))
    return password


print(get_random_password())

