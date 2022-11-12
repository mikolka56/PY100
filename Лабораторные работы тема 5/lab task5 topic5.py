import random
import string
str_ = string.digits + string.ascii_lowercase + string.ascii_uppercase
n = 8
def get_random_password(n: int) -> str:
    for x in range(n):
        password = "".join(random.sample(str_, n))
    return password
print(get_random_password(n))

