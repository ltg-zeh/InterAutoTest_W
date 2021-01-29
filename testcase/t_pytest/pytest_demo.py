import pytest

# 1.创建测试方式
'''
1.创建普通方法
2.创建断言方法
'''
# 创建普通方法
def func(x):
    return x+1

#创建断言的方法
def test_a():
    print("----test_a-----")
    assert func(3) == 5

def test_b():
    print("----test_b-----")
    assert 1

# 2.pytest运行
# 代码直接运行
if __name__ == '__main__':
    pytest.main(["pytest_demo"])
