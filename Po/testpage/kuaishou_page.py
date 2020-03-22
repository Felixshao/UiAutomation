from time import sleep

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
        if flag:
            while True:
                self.app.slipe_up_window()
                sleep(10)