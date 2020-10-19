import pytest,yaml

class TestDemo:

    @pytest.mark.parametrize("env", yaml.safe_load(open('./env.yaml')))
    def test_demo1(self, env):
        if 'test' in env:
            print('这是测试环境')
            print(env['test'])
        elif 'dev' in env:
            print('这是开发环境')
            print(env['dev'])





























