import os
# 1.获取醒目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)

# 定义config目录路径
_config_path = BASE_DIR + os.sep + "config"
# 定义conf.yml文件路径
_config_file = _config_path + os.sep + "conf.yml"

def get_config_path():
    return _config_path

def get_confug_file():
    return _config_file

# 读取配置文件
class ConfigYaml:
# 初始化yaml读取配置文件
    def __init__(self):