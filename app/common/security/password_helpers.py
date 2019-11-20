import string
import random

def password_generate(lenght=8):
    letters = string.hexdigits
    return ''.join(random.choice(letters) for i in range(lenght))