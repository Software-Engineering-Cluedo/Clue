import unittest
from src.cli import Cli


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cli = Cli()
        cli.test_movement()
        #self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
