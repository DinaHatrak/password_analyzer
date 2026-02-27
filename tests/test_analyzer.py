import unittest
from src.nist_check import check_password_nist
from analysis.entropy import calculate_entropy

class TestPasswordProject(unittest.TestCase):

    def test_nist_weak_password(self):
        # Testing a password that is too short
        is_valid, msg = check_password_nist("123")
        self.assertFalse(is_valid)

    def test_nist_strong_password(self):
        # Testing a compliant password
        is_valid, msg = check_password_nist("Dina_Secure_2026!")
        self.assertTrue(is_valid)

    def test_entropy_logic(self):
        # Ensuring simple passwords have low entropy scores
        score = calculate_entropy("password")
        self.assertLess(score, 40)

if __name__ == "__main__":
    unittest.main()
