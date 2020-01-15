import os
from config.getProjectPath import get_project_path
from common.BeautifulReport import BeautifulReport
from common.log import Logger

path = get_project_path()
log = Logger('common.basePage').get_logger()


class Page(object):

    def __init__(self, driver, img_path=os.path.join(path, 'report', 'screen_shot')):

        self.dr = driver
        self.img_path = img_path
