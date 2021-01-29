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
    assert func(3) == 5  # 断言失败1
# 执行3次，等待2秒
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_c():
    print("----test_c----")
    assert func(2) == 5  # 断言失败2

def test_b():
    print("----test_b-----")
    assert 1

# 2.pytest运行
# 代码直接运行
if __name__ == '__main__':
    pytest.main(["pytest_demo.py"])
