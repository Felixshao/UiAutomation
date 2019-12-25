import os
from config.getProjectPath import get_project_path
from common.BeautifulReport import BeautifulReport

path = get_project_path()


class Page(object):

    def __init__(self, driver):

        self.dr = driver
        self.img_path = os.path.join(path, 'report', 'screen_shot')