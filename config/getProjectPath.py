import os


def get_project_path():
    """
    获取项目路径
    :return: 返回项目路径
    """
    current_path = os.path.split(os.path.realpath(__file__))[0]     # 获取当前文件的目录路径
    project_path = os.path.abspath(os.path.dirname(current_path))   # 获取项目路径并返回绝对路径

    return project_path
