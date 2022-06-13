import unittest
from concurrent.futures import ThreadPoolExecutor

class Runner():

    def parallel_execution(self, *name):
        suite = unittest.TestSuite()

        for object in name:
            for method in dir(object):
                if (method.startswith('test')):
                    suite.addTest(object(method))

        with ThreadPoolExecutor(max_workers=10) as executor:
            runner = unittest.TextTestRunner()
            list_of_suites = list(suite)
            for test in range(len(list_of_suites)):
                test_name = str(list_of_suites[test])
                executor.submit(runner.run, list_of_suites[test])
