import hashlib
import random
import string

from user_service.settings import settings


def get_random_string(length=12):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(password: str, salt: str = settings.SECRET_KEY):
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


def verify(plain_password, hashed_password):
    return hash_password(plain_password) == hashed_password



