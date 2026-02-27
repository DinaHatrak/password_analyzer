import unittest
from src import analyzer

class TestAnalyzer(unittest.TestCase):
    def test_main_runs(self):
        try:
            analyzer.main()
            ran_successfully = True
        except Exception:
            ran_successfully = False
        self.assertTrue(ran_successfully)

if __name__ == "__main__":
    unittest.main()
