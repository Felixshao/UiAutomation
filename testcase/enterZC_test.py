from common import Mybrowser
from testpage.enterZC_page import enterZC_page


class enterZC(Mybrowser.Mybrowser):

    def test1_enterZC(self):

        enterpage = enterZC_page(self.dr)
        enterpage.into_ZC()
        enterpage.click_login_button()
        enterpage.input_user_name()
        enterpage.input_password()
        enterpage.click_login()
        enterpage.click_parttime_task()
        # enterpage.swipe_page()
        enterpage.click_filter_task()
        enterpage.click_task()

    def test2_print(self):
        """调试截图"""
        self.dr.open_url('https://www.baidu.com')
        self.dr.get_page_screenshot('d:\\study\\python\\UiAutomation\\report\\screen_shot\\LauncherUI_我的.png', 'LauncherUI_我的.png')



