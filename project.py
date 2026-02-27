from analysis import entropy, brute_force
from src import nist_check

def main():
    # Test password
    password = "Dina_Security_2026!" 
    
    print(f"--- Password Analysis for: {password} ---")

    # 1. Calculate Shannon Entropy
    entropy_value = entropy.calculate_entropy(password)
    print(f"Entropy Score: {entropy_value} bits")
    
    # 2. Check NIST Compliance
    # The function returns a tuple: (Boolean, Feedback)
    nist_status, nist_msg = nist_check.check_password_nist(password)
    print(f"NIST Compliance: {nist_status}")
    print(f"Feedback: {nist_msg}")

    # 3. Estimate Brute Force Cracking Time
    # We pass the entropy value to the estimation function
    time_result = brute_force.estimate_cracking_time(entropy_value)
    print(f"Estimated Cracking Time: {time_result}")

if __name__ == "__main__":
    main()
