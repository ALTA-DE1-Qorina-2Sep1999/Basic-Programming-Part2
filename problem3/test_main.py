import unittest
from main import luas_permukaan_tabung

class TestLuasFunction(unittest.TestCase):
    def test_luas_pertama(self):
        self.assertEqual(luas_permukaan_tabung(4, 20), 602.88)

if __name__ == '__main__':
    unittest.main()