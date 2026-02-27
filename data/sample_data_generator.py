import pandas as pd

def generate_sample_data():
    data = {
        'password': ['123456', 'Admin@2026', 'Dina_Security_2026', 'password'],
        'category': ['Weak', 'Medium', 'Strong', 'Weak']
    }
    
    df = pd.DataFrame(data)
    df.to_csv('data/passwords.csv', index=False)
    print("Data file created successfully in data/ folder.")

if __name__ == "__main__":
    generate_sample_data()
