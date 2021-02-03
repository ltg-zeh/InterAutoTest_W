import pytest

# 判断为真
def test_1():
    a = True
    assert a

# 判断不为真
def test_2():
    a = True
    assert not a

# 判断b包含a
def test_3():
    a = "zeh"
    b = "lzehtg"
    assert a in b

# 判断相等
def test_4():
    a = 1
    b = 1
    assert a == b

# 判断不相等
def test_5():
    a = 1
    b = 2
    assert a != b


if __name__ == '__main__':
    pytest.main(["pytest_assert.py"])