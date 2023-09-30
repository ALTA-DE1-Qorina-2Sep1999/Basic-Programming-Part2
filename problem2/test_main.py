import unittest
from main import luas_segitiga

class TestLuasFunction(unittest.TestCase):
    def test_luas_pertama(self):
        self.assertEqual(luas_segitiga(20.0, 25.0), 250)

if __name__ == '__main__':
    unittest.main()