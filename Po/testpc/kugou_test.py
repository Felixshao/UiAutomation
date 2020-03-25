import unittest, time
from common.MySelenium import mySelenium
from Po.testpage.kugou_page import kugou_page
from config.readConfig import readConfig

kugou_path = readConfig().get_exe()['kugou']
backend = 'uia'
title = '酷狗音乐'
class_name = 'kugou_ui'


class kugou_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = mySelenium()
        cls.dr.open_pc_exe(file_path=kugou_path, title=title, class_name=class_name, backend=backend)
        cls.kg = kugou_page(cls.dr)

        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1_play_muisc(self):
        """酷狗播放音乐"""
        self.kg.kugou_play_music()

    def test1_unplay_muisc(self):
        """酷狗暂停音乐"""
        time.sleep(10)
        self.kg.kugou_play_music()