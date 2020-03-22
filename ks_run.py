import unittest
from Po.testapp.kuaishou_test import kuaishou_test


def run():
    suite = unittest.TestSuite()
    suite.addTest(kuaishou_test('test1_slide_window'))
    runny = unittest.TextTestRunner(verbosity=2)
    runny.run(suite)


if __name__ == '__main__':

    run()