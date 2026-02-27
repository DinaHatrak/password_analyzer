from analysis import entropy, brute_force
from src import nist_check

def main():
    password = "Example123!"
    print("Analyzing password:", password)

    entropy_value = entropy.calculate_entropy(password)
    print("Entropy:", entropy_value)
   
    nist_result = nist_check.check_password(password)
    print("NIST compliance:", nist_result)

    brute_force_time = brute_force.estimate_time(password)
    print("Brute force time:", brute_force_time)

if __name__ == "__main__":
    main()
