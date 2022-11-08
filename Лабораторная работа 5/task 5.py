from random import sample
import string


def get_random_password(n=8) -> str:
    alphabet = string.ascii_uppercase + string.digits + string.ascii_lowercase
    password = "".join(sample(alphabet, n))
    return password


print(get_random_password())

