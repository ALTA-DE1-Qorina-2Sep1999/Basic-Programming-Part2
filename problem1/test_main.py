import unittest
from main import nama

class TestNamaFunction(unittest.TestCase):
    def test_nama_with_input_kober(self):
        self.assertEqual(nama("Kobar"), "Hello Kobar! Saya Golang bahasa yang sangat menyenangkan!")

if __name__ == '__main__':
    unittest.main()