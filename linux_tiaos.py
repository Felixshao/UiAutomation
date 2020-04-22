import platform
from selenium import webdriver
from pyvirtualdisplay import Display

if platform.system() != 'Windows':
    print(1)
else:
    print(2)
# display = Display(visible=0, size=(900, 800))
# display.start()
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# print('linux tiaos')
