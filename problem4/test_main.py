import unittest
from main import bayar

class TestLuasFunction(unittest.TestCase):
    def test_bayar(self):
        self.assertEqual(bayar(370000, 15), 314500)

if __name__ == '__main__':
    unittest.main()