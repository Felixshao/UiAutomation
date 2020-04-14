import unittest
import threading
import multiprocessing as mp
from Po.testinterface.Stockinter_test import Stockinter_test
from Po.testapp.tgpIntergral_test import tgpIntergral_test


def run(case):
    suite = unittest.TestSuite()
    suite.addTest(case)
    runny = unittest.TextTestRunner(verbosity=1)
    runny.run(suite)


def process():
    pool = mp.Pool()
    cases = [Stockinter_test('test1_Lushang_stock'), Stockinter_test('test2_chinaSatcom_stock'),
             Stockinter_test('test3_xinlong_stock'), Stockinter_test('test4_chinabaoan_stock'),
             Stockinter_test('test5_twosixthree_stock')]
    for i in range(len(cases)):
        pool.apply_async(run, args=(cases[i],))
    pool.close()
    pool.join()


def process2():
    pool = mp.Pool()
    cases = [tgpIntergral_test('test1_intergral_checkIn'), tgpIntergral_test('test2_intergral_treasure')]
    for i in range(len(cases)):
        pool.apply_async(run, args=(cases[i],))
    pool.close()
    pool.join()


def threaad():
    cases = [Stockinter_test('test1_Lushang_stock'), Stockinter_test('test2_chinaSatcom_stock'),
             Stockinter_test('test3_xinlong_stock'), Stockinter_test('test4_chinabaoan_stock'),
             Stockinter_test('test5_twosixthree_stock')]
    thread1 = threading.Thread(target=run, args=(cases[0],))
    thread2 = threading.Thread(target=run, args=(cases[1],))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == '__main__':
    process()