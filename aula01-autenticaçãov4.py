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

reallypassword = input("Enter your password: ")

if __name__== "__main__":
    hashed = hash(f"{reallypassword}")
    print(f"Hashed password: {hashed}")
    print(f"Verify correct password: {verify(f"{reallypassword}", hashed)}")