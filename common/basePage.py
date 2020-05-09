import os
from config.getProjectPath import get_project_path
from common.log import Logger

path = get_project_path()
log = Logger('common.basePage').get_logger()


class Page(object):

    def __init__(self, driver, img_path=os.path.join(path, 'report', 'screen_shot'), uiau=None, app=None):

        self.dr = driver
        self.img_path = img_path
        self.uiau = uiau
        self.app = app
