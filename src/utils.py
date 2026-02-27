import hashlib

def hash_password(password):
    # Standard security practice to store passwords as hashes
    return hashlib.sha256(password.encode()).hexdigest()
