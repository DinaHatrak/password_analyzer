def estimate_time(password: str) -> str:

    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32

    combinations = charset_size ** len(password)
    attempts_per_second = 1_000_000_000
    seconds = combinations / attempts_per_second

    return f"{seconds:.2e} seconds"

