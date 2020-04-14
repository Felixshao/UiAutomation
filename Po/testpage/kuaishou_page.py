import time
from time import sleep
import random

ks_comment_button = 'id->com.kuaishou.nebula:id/comment_button'


class kuaishou_page(object):
    def __init__(self, app):
        self.app = app

    def ks_click_comment(self):
        self.app.click(ks_comment_button)

    def ks_slide_window(self):
        """向上滑动窗口"""
        self.app.app_background()
        flag, ele = self.app.judge_element(ks_comment_button)
        t = time.time()
        if flag:
            hour = random.randint(1800, 3600)
            while True:
                t2 = time.time()
                if t2 - t < hour:
                    sec = random.randint(2, 10)
                    if sec % 2 == 0:
                        self.app.slipe_up_window()
                    else:
                        self.app.slipe_under_window()
                    sleep(sec)
                else:
                    secs = random.randint(5, 20)
                    self.app.app_background(secs=secs)
                    self.ks_slide_window()


if __name__ == '__main__':

    pass