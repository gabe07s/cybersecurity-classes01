#codificação de senha
from argon2 import PasswordHasher

SALT = 'J6dT30s@L7'

ph = PasswordHasher()

def hash(password):
    return ph.hash(password + SALT)

def verify(password, hashed):
    try:
        ph.verify(hashed, password + SALT)
        return True
    except:
        return False

if __name__== "__main__":
    hashed = hash('banana')
    print(f"Hashed password: {hashed}")
    print(f"Verify correct password: {verify("banana", hashed)}")