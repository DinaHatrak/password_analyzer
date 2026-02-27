def check_password_nist(password: str):

    reasons = []
    
    # Length Check
    if len(password) < 8:
        reasons.append("Password is too short. It should be at least 8 characters.")
        
    # Complexity Check
    if password.isalpha():
        reasons.append("Add numbers or symbols to make it stronger.")
    if password.isnumeric():
        reasons.append("Add letters to prevent easy cracking.")

    if not reasons:
        return True, "Your password follows NIST standards. Well done!"
    else:
        return False, reasons
