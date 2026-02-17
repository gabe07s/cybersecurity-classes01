#codificação de senha

from hashlib import sha256
import secrets

SALT = 'J6dT30s@L7'

def hash(password, pepper=''):
    if not pepper:
        pepper = secrets.token_hex(16)
    to_hash = (pepper + SALT + password).encode()
    return pepper + ',' + sha256 (to_hash).hexdigest()

def verify(password, hashed):
    pepper, _ = hashed.split(',')
    return hash(password, pepper) == hashed

if __name__== "__main__":
    hashed = hash('banana')
    print(f"Hashed password: {hashed}")
    print(f"Verify correct password: {verify("banana", hashed)}")