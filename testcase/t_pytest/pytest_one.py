
# coding=gbk
import pytest
'''
1.������Ͳ��Է���
2.��������
3.����������
4.����
'''
# 1.������Ͳ��Է���
class TestDemo:

    # 2.������������
    data_list = ["ltg","zeh"]

    #3.������
    @pytest.mark.parametrize("name",data_list)
    def test_a(self,name):
        print("test_a")
        print(name)
        assert 1

if __name__ == '__main__':
    pytest.main(["pytest_one.py"])