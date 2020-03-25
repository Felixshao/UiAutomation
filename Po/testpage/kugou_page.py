from common.log import Logger

log = Logger('Po.testpage.kugou_page').get_logger()
title = '酷狗音乐'
class_name = 'kugou_ui'
""" ----------------------------------------------------------------------------------------------------- """
kg_play_music = u'播放/暂停"'   # 酷狗音乐窗口播放按钮


class kugou_page():

    def __init__(self, driver):

        self.dr = driver

    def kugou_play_music(self):
        """"点击酷狗卜播放/暂停按钮"""
        # self.dr.get_exe_controls(title=name)
        self.dr.click_exe(control=kg_play_music, title=title, class_name=class_name)
        log.info('Success点击播放/暂停按钮')

