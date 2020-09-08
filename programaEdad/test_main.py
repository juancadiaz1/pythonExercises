import unittest

from main import saberEdad


class Test(unittest.TestCase):
    def test_saberEdad(self):
        self.assertEqual(72,saberEdad(1998,0))

if __name__ == '__main__':
    unittest.main()
