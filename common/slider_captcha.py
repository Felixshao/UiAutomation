import cv2, os
import time
from config.getProjectPath import get_project_path
from common.log import Logger
from common.MySelenium import mySelenium

log = Logger('common.slider_captcha.py').get_logger()
path = get_project_path()   # 项目路径
captcha_background = os.path.join(path, 'report', 'screen_shot', 'captcha_background.png')      # 验证码背景图
captcha_background_crop = os.path.join(path, 'report', 'screen_shot', 'captcha_background_crop.png')    # 裁剪后的背景图
captcha_background_canny = os.path.join(path, 'report', 'screen_shot', 'captcha_background_canny.png')      # 背景图canny化
captcha_puzzle = os.path.join(path, 'report', 'screen_shot', 'captcha_puzzle.png')  # 验证码拼图块
captcha_puzzle_crop = os.path.join(path, 'report', 'screen_shot', 'captcha_puzzle_crop.png')     # 裁剪后的拼图块
captcha_puzzle_canny = os.path.join(path, 'report', 'screen_shot', 'captcha_puzzle_canny.png')      # 拼图块canny化


def canny(background_crop, puzzle_crop):
    """
    匹配图片，计算缺口位置
    :param background_crop:验证码背景图
    :param puzzle_crop:验证码拼图
    :return:max_loc返回缺口坐标
    """
    imgs = []
    # 原始图像，用于展示
    sou_img1 = cv2.imread(background_crop)
    sou_img2 = cv2.imread(puzzle_crop)

    # 原始图像，灰度
    # 最小阈值100,最大阈值500
    img1 = cv2.imread(background_crop, 0)
    blur1 = cv2.GaussianBlur(img1, (3, 3), 0)
    canny1 = cv2.Canny(blur1, 100, 500)
    cv2.imwrite(captcha_background_canny, canny1)

    img2 = cv2.imread(puzzle_crop, 0)
    blur2 = cv2.GaussianBlur(img2, (3, 3), 0)
    canny2 = cv2.Canny(blur2, 100, 500)
    cv2.imwrite(captcha_puzzle_canny, canny2)

    target = cv2.imread(captcha_background_canny)
    template = cv2.imread(captcha_puzzle_canny)

    # 调整显示大小
    target_temp = cv2.resize(sou_img1, (350, 200))
    target_temp = cv2.copyMakeBorder(target_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    template_temp = cv2.resize(sou_img2, (200, 200))
    template_temp = cv2.copyMakeBorder(template_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp)
    imgs.append(template_temp)

    # 匹配拼图
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

    # 归一化
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    log.info('成功得出移动距离')
    # 查看匹配后结果并画圈
    # theight, twidth = template.shape[:2]
    # cv2.rectangle(target, max_loc, (max_loc[0] + twidth, max_loc[1] + theight), (0, 0, 255), 2)
    #
    # target_temp_n = cv2.resize(target, (350, 200))
    # target_temp_n = cv2.copyMakeBorder(target_temp_n, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    #
    # imgs.append(target_temp_n)
    # imstack = np.hstack(imgs)
    # cv2.imshow('stack' + str(max_loc), imstack)
    # cv2.waitKey(0)

    # 计算出拖动距离
    distance = int(max_loc[0] / 2 - 27.5) + 2
    log.info('成功得出移动距离: {}'.format(distance))
    return distance


def slider_captcha(browser, handle, tcaptcha_iframe='tcaptcha_iframe', slideBg='id->slideBg', slideBlock='id->slideBlock',
                   tcaptcha_drag_thumb='id->tcaptcha_drag_thumb'):
    """
    缺口滑块验证码滑动
    :param browser:driver
    :param handle:登录页面句柄
    :param tcaptcha_iframe:滑块验证码的ifram
    :param slideBg: 背景图元素（格式：id->slideBg）
    :param slideBlock: 拼图块元素
    :param tcaptcha_drag_thumb: 滑块id
    :return:
    """
    time.sleep(1)

    # 获取背景图src
    targetUrl = browser.get_element_attribute(slideBg, 'src')

    # 获取拼图块src
    tempUrl = browser.get_element_attribute(slideBlock, 'src')

    # 新建标签页
    browser.js("window.open('');")
    # 切换到新标签页
    browser.switch_handle(browser.get_handles()[1])

    # 访问背景图src
    browser.open_url(targetUrl)
    time.sleep(3)
    # 截图保存背景图
    browser.get_page_screenshot(case_name='captcha_background')
    log.info('成功保存验证码背景图: "{}"'.format(captcha_background))
    # 背景图宽高
    w = 680
    h = 390
    # 加载背景图
    img = cv2.imread(captcha_background)
    # 获取图片高框
    size = img.shape
    # 计算出图片位置
    top = int((size[0] - h) / 2)
    height = int(h + top)
    left = int((size[1] - w) / 2)
    width = int(w + left)

    cropped = img[top:height, left:width]

    # 裁剪出背景图
    cv2.imwrite(captcha_background_crop, cropped)
    log.info('成功裁剪验证码背景图: "{}"'.format(captcha_background_crop))
    # 新建标签页
    browser.js("window.open('');")

    browser.switch_handle(browser.get_handles()[2])

    browser.open_url(tempUrl)
    time.sleep(3)
    # 截图保存拼图块
    browser.get_page_screenshot(case_name='captcha_puzzle')
    log.info('成功保存验证码拼图块: "{}"'.format(captcha_puzzle))
    # 拼图块宽高
    w = 136
    h = 136
    # 加载拼图
    img = cv2.imread(captcha_puzzle)
    # 获取拼图高宽
    size = img.shape
    # 计算出图片位置
    top = int((size[0] - h) / 2)
    height = int(h + top)
    left = int((size[1] - w) / 2)
    width = int(w + left)

    cropped = img[top:height, left:width]
    # 裁剪拼图并保存
    cv2.imwrite(captcha_puzzle_crop, cropped)
    log.info('成功裁剪验证码拼图块: "{}"'.format(captcha_puzzle_crop))

    browser.switch_handle(handle)
    time.sleep(2)
    browser.switch_iframe(tcaptcha_iframe)

    # 模糊匹配两张图片，获取缺块位置
    move = canny(captcha_background_crop, captcha_puzzle_crop)
    # 计算循环次数
    if move % 10 == 0:
        num = 10
    else:
        num = 11
    browser.move_offset(tcaptcha_drag_thumb, move, 0, num, 10)

    time.sleep(2)
    # 通过验证码背景图是否还存在来判断是否通过，未通过重复进行
    if isEleExist(browser, slideBg):
        slider_captcha(browser, handle)
        log.info('滑块拼图验证失败，重新验证!')
    else:
        handles = browser.get_handles()
        for i in range(1, len(handles)):
            browser.close_window(handles[i])
        browser.switch_handle(handles[0])


def isEleExist(browser, id):
    """
    断言元素是否存在
    :param browser:driver
    :param id:id
    :return:True or False
    """
    try:
        browser.find_element(id)
        return True
    except:
        return False


# 小鹅通滑块测试
def test():
    browser = mySelenium()
    browser.browser()

    # 网站登陆页面
    url = 'https://admin.xiaoe-tech.com/login_page?reg_source=0101&xeuti=ituex#/acount'

    # 浏览器访问登录页面
    browser.open_url(url)

    handle = browser.get_current_handle()

    # 点击登陆按钮，弹出滑动验证码
    browser.send('xpath->//div[@class="phoneWrapper"]/div/input', '15779582092')
    browser.send('xpath->//div[@class="passwordWrapper"]/div/input', '123456')
    browser.click('class->login-btn')
    browser.switch_iframe('tcaptcha_iframe', 2)
    slider_captcha(browser, handle)
    time.sleep(10)
    print(browser.get_cookies())


if __name__ == '__main__':
    test()