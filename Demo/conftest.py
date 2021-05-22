import pytest


@pytest.fixture()
def connect_db():
    print('连接数据库')
    yield '搜索结果'
    print('断开数据库')


@pytest.fixture(scope='module')
def login():
    print('登录')
    balance = 1000
    score = 5
    return balance, score


def pytest_collection_modifyitems(session, config, items):
    print("所有将执行的测试用例：")
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode("utf-8").decode('unicode-escape')
