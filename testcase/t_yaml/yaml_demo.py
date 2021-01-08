# 1.创建yaml格式文件
# 2.读取文件
# 3.输出文件

import yaml
# 读取单个文件
# with open("./data.yaml",encoding='utf-8') as f:
#     r = yaml.safe_load(f)
#     print(r)

# 读取多个文件
with open("./data.yaml","r",encoding='utf-8') as f:

    r = yaml.safe_load_all(f)
    for i in r:
        print(i)