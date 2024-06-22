import unittest
from salt.modules.disk import _parse_numbers

class TemptestDisk (unittest.TestCase):
    def test_parse_2(self):
        self.assertEqual(_parse_numbers("2"), 2)
    def test_parse_K(self):
        self.assertEqual(_parse_numbers("10K"),10000)
    def test_parse_M(self):
        self.assertEqual(_parse_numbers("10M"),10000000)
    def test_parse_Y(self):
        self.assertEqual(_parse_numbers("5Y"),5000000000000000000000000)

if __name__=='__main__':
    unittest.main()
