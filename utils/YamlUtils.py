import os

class YamlReader:
    # 初始化，文件是否存在
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")

    # yaml读取
    def data(self):
        pass