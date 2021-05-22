import allure
import pytest
import yaml


def test_getdata():
    with open("./Data/data.yaml", encoding='utf-8') as s:
        data = yaml.safe_load(s)
    return data


@allure.feature('计算器')
class TestData:
    # 参数化、ids用例名
    @pytest.mark.parametrize("a,b", [(1, 2), (200000, 300000)], ids=['小数字', '大数字'])
    @allure.story('parametrize参数化')
    def test_add(self, a, b):
        print(a + b)

    # # yaml参数化
    # @pytest.mark.parametrize("a, b", yaml.safe_load(open("../Data/data.yaml", encoding='utf-8')))
    # def test_add_yaml(self, a, b):
    #     print(a + b)

    #  yaml参数化
    @pytest.mark.parametrize("a, b", test_getdata()['add_data'], ids=test_getdata()['ids'])
    @allure.story('yaml参数化')
    def test_add_yaml(self, a, b):
        print(a + b)
