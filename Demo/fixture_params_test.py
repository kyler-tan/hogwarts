import allure
import pytest


@pytest.fixture(params=[['张三', 123], ['李四', 123], ['王五', 123]], ids=['张三', '李四', '王五'])
def login(request):
    return request.param


@allure.story('登录测试用例')
def test_login(login):
    print(login)
