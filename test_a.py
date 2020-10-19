# import os,sys
# sys.path.append(os.getcwd())
# pytest运行时没有检索当前目录自己导入的模块  - 可以加上这两段代码

import pytest


@pytest.fixture()
def login():
    a = 1
    b = 9
    s = a + b
    print(f'最后结果等于{s}')
    return s


class TestDemo:

    @pytest.mark.usefixtures('login')
    def test_master(self, login):
        print(login)
        print('12233')

    def test_sub(self):
        print('222222')

# if __name__ == '__main__':
#     pytest.main(['test_a.py::TestDemo::test_sub','-vs'])
#     # test_master(login)






































