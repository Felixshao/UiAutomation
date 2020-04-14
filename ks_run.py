import unittest
from Po.testapp.kuaishou_test import kuaishou_test
from pywinauto import application


def run():
    suite = unittest.TestSuite()
    suite.addTest(kuaishou_test('test1_slide_window'))
    runny = unittest.TextTestRunner(verbosity=2)
    runny.run(suite)


def open_pc():
    app = application.Application(backend='uia')
    app.start('C:/Program Files (x86)/Appium/Appium.exe')
    print(app)


if __name__ == '__main__':
    run()