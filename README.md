

# Password Security Analyzer  

## Description  
A comprehensive Python tool designed to evaluate password strength using **Shannon entropy**, **NIST standards**, and brute force estimation. This project was developed as part of the **CS50 Cybersecurity curriculum** to demonstrate secure coding practices, data analysis, and practical password evaluation.  

---

## Project Structure  
- **project.py** → The main entry point of the application.  
- **analysis/** → Contains logic for Shannon Entropy calculation and brute force cracking time estimation.  
- **src/** → Includes NIST compliance checks and security utilities.  
- **tests/** → Unit tests to ensure code reliability and maintainability.  

---

##  How to Run  
Run the main script from the terminal:  
```bash
python project.py
```

You will be prompted to enter a password. The analyzer will then generate a detailed report including:  
- **Entropy Score** (measures randomness and complexity).  
- **NIST Compliance** (checks against recommended standards).  
- **Feedback** (suggestions for improvement).  
- **Estimated Cracking Time** (approximate time needed for brute force attacks).  

---

##  Example Output  
```bash
Enter password: Tr0ub4dor&3
--- Password Analysis for: Tr0ub4dor&3 ---
Entropy Score: 65.42 bits
NIST Compliance: True
Feedback: ['Strong password!', 'Consider adding more special characters for maximum security.']
Estimated Cracking Time: 2.5 Years
```

---

## Key Features  
- Evaluates password strength using **mathematical entropy**.  
- Validates compliance with **NIST password standards**.  
- Estimates cracking time against brute force attacks.  
- Provides actionable **feedback** to improve password security.  
- Includes **unit tests** for reliability.  

---

## Dependencies  
This project uses only Python standard library. No external dependencies are required.  

---

## Running Tests  
To run the unit tests:  
```bash
python -m unittest discover tests
```
