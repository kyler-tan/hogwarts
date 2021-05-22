import pytest


def test_search(connect_db):
    print('搜索')


@pytest.mark.usefixtures('login')
def test_add_cart():
    print('添加购物车')


def test_order(login, connect_db):
    print('订单')
    b, s = login
    print(b, s)
