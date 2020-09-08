import unittest

from main import calcularDescuento


class Test(unittest.TestCase):

    def test_calcularDescuento(self):
        self.assertEqual(45.0, calcularDescuento(50, 'l'))


if __name__ == '__main__':
    unittest.main()
