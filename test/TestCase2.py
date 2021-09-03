import unittest
from logs.log import logger


class TestCalc(unittest.TestCase):

    def test_sum(self):
        assert sum([1, 2, 3]) == 6
        logger.debug("Test1 : Should be 6")

    def test_sum_tuple(self):
        assert sum((1, 2, 2)) == 6
        logger.debug("Test2: Should be 6")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    unittest.main()
