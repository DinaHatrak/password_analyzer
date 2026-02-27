import math

def calculate_entropy(password: str) -> float:

    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32  

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)
