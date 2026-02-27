def check_password(password: str) -> bool:
 
    if len(password) < 8:
        return False
    if password.isalpha() or password.isnumeric():
        return False
    return True
