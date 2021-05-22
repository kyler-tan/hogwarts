import pytest

# 测试用例执行顺序

@pytest.mark.run(order=2)
def test_too():
    assert True


@pytest.mark.run(order=1)
def test_one():
    assert True



