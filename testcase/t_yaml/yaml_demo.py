# 1.创建yaml格式文件
# 2.读取文件
# 3.输出文件

import yaml

with open("./data.yaml") as f:
    r = yaml.safe_load(f)
    print(r)
    print(r)