from suite import CustomTestSuite
from test import ConcurrencyTest
import unittest


if __name__ == '__main__':
    suite = CustomTestSuite()

    for method in dir(ConcurrencyTest):
        if (method.startswith('test')):
            suite.addTest(ConcurrencyTest(method))

    unittest.TextTestRunner(verbosity=2).run(suite)
