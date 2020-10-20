# __author:liujinfang5
# data: 2020/10/19
import os

import pytest
import yaml


# 获取yml文件中的测试数据
def get_datas():
    """
    获取yml文件中的数据
    :return:
    """
    # 绝对路径
    # file_name = "D:\\XX\\workspace\\deliverytest\\demo\\data\\cacl.yml"
    # file_name = os.getcwd() + "\cacl.yml"
    # 相对路径
    file_name ="./data/cacl.yml"
    with open(file_name) as f:
        # 只能load一次，load成功后去load第二次就没有数据了
        datas = yaml.safe_load(f)
    return datas["add"]["datas_float"], datas["add"]["ids_float"], datas["add"]["datas_int"], datas["add"]["ids_int"], datas["div"]["datas_int"], datas["div"]["ids_int"], datas["div"]["datas_zero"], datas["div"]["ids_zero"], datas["div"]["datas_float"],datas["div"]["ids_float"],


class TestOperation:
    # def setup(self):
    #     print("开始计算")
    #     self.cal=Calculator()
    #
    # def teardown(self):
    #     print("计算结束")

    # 测试加法，整数和空值
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('m,n,expect', get_datas()[2], ids=get_datas()[3])
    def test_sum(self, get_cals, m, n, expect):
        # result=self.cal.sum(m, n)
        result = get_cals.sum(m, n)
        assert result == expect

    # 测试加法，浮点数
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('m,n,expect', get_datas()[0], ids=get_datas()[1])
    def test_sum_float(self, get_cals,  m, n, expect):
        # result=self.cal.sum(m, n)
        result = get_cals.sum(m, n)
        assert round(result, 3) == expect

    # 测试除法整数
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('m,n,expect', get_datas()[4], ids=get_datas()[5])
    def test_div(self, get_cals, m, n, expect):
        # result=self.cal.div(m, n)
        result = get_cals.div(m, n)
        assert result == expect

    # 除数为0的case
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('m,n,expect', get_datas()[6], ids=get_datas()[7])
    def test_div_zero(self, get_cals, m, n, expect):
        # python 处理异常，如果不是这个异常，走到这个case会报错，是这个异常，会展示case通过
        with pytest.raises(ZeroDivisionError):
            result=get_cals.div(m, n)
            # result=self.cal.div(m, n)

    # 浮点数除法测试用例
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('m,n,expect', get_datas()[8], ids=get_datas()[9])
    def test_div_float(self, get_cals, m, n, expect):
        # result=self.cal.div(m, n)
        result = get_cals.div(m, n)
        assert round(result, 2) == expect