import os
from utils.YamlUtils import YamlReader
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
# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"

def get_config_path():
    return _config_path

def get_confug_file():
    return _config_file

def get_log_path():
    '''
    获取log文件路径
    :return:
    '''
    return _log_path

# 读取配置文件
class ConfigYaml:
# 初始化yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_confug_file()).data()

    # 获取所需要的信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    print(conf_read.get_conf_log())
    print(conf_read.get_conf_log_extension())