from common.Mymoible import Mymobile
from testpage.enterApp_page import enterApp_page


class enterApp_test(Mymobile):

    def test1_openApp(self):

        app = enterApp_page(self.dr)
        app.qq_login()

