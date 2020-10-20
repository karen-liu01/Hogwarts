import re


# 被测的方法
class Calculator:
    # 判断输入是否为数字
    def is_number(self, a):
        """
        判断输入是否为数字，是返回True，不是返回False
        :param a:
        """
        value=re.compile(r'^[-+]?[0-9]+\.*[0-9]*$')
        result=re.match(value, str(a))
        if result:
            # 是数字
            return True
        else:
            # 不是数字
            return False

    # 判断m是否为空字符串
    def is_empty(self, m):
        """
        判断m是否为空字符串，是返回True，不是返回False
        :param m:
        :return:
        """
        if not len(str(m)):
            # 输入是空
            return True
        else:
            # 输入不是空
            return False

    # 加
    def sum(self, a, b):
        if self.is_empty(a) or self.is_empty(b):
            print("参与运算的参数不能为空")
            return 0
        elif not (self.is_number(a) and self.is_number(b)):
            print("输入的参数必须为数字")
            return 0
        else:
            return a + b

    # 减
    def sub(self, a, b):
        return a - b

    # 乘
    def mul(self, a, b):
        return a * b

    # 除,除数为0的处理在测试case中了
    def div(self, a, b):
        if self.is_empty(a) or self.is_empty(b):
            print("参与运算的参数不能为空")
            return 0
        elif not (self.is_number(a) and self.is_number(b)):
            print("输入的参数必须为数字")
            return 0
        else:
            return a / b


# 单测
class TestC:
    cal1=Calculator()
    # print(cal1.is_number(0))
    # print(cal1.is_number(-1))
    # print(cal1.is_number(1))
    # print(cal1.is_number(1.1))
    # print(cal1.is_number('a'))