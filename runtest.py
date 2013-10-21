import unittest


def load_tests(_, __, ___):
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('test',
                                                              pattern='*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()
