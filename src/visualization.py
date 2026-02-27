import matplotlib.pyplot as plt

def plot_password_strength(entropy_value):
    labels = ['Your Password', 'Strong Standard']
    values = [entropy_value, 80]  # 80 bits is considered strong
    
    plt.bar(labels, values, color=['pink', 'skyblue'])
    plt.ylabel('Entropy (Bits)')
    plt.title('Password Strength Analysis')
    plt.axhline(y=60, color='red', linestyle='--', label='Minimum Secure')
    plt.show()
