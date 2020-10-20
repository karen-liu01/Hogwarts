# __author:liujinfang5
# data: 2020/10/20
# pytest test_fixture.py --setup-show -vs
from typing import List

import pytest
from demo.calculator import Calculator


# 测试test_operation需要用的装饰器
@pytest.fixture(scope="module")
def get_cals():
    cal = Calculator()
    print("开始计算")
    yield cal
    print("结束计算")


# 测试装饰器  将fixture传到装饰器中，不可以使用fixture的返回值;参数化可见例子
@pytest.fixture(scope="session", autouse=True, params=["username", "password"])
def login(request):
    # 相当于setup
    print("1111")
    # 相当于return
    username = request.param
    yield username
    # 相当于teardown
    print("2222")


# # 收集测试用例，统一处理，比如编码格式等  改写hook函数
# # def pytest_collection_modifyitems(session, config, items):
# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     for item in items:
#         item.name = items.name.encode("utf-8").decode("unicode-escape")
#         item._nodeid = items.nodeid.encode("utf-8").decode("unicode-escape")