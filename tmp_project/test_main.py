# test_xxx：仿照 pytest ，文本解析
# hello.a：
# 动态导入：c = importlib.import_module(“hello”)
# 反射： getattr(c, ‘a’)()
# re.search：导入特定包下面的模块tmp = “a.b.c.d.f”.split(".")
# save： globals()[“a”] = 101 ，print(globals()[“a”])
# [$(tmp)]：
# 怎么取到 tmp：globals()[‘tmp’]
# 怎么把 string 当成 python 命令调用： a = 1 ; print(eval(“a”))
import yaml


class TestMain:
    # 解析yaml文件,并且将数据返回
    def load_data(self):
        with open("./tmp.yaml") as f:
            datas = yaml.safe_load(f)
            # print(datas)
        return datas

    # 处理yaml中的数据
    def handle_datas(self, datas: dict):
        # 1.先取到字典所有的key
        # 2.然后判断key是不是以test开头,如果是，执行case，如果不是，不执行
        for key in datas.keys():
            # print(key)
            if key.startswith("test_"):
                print(f"测试用例的名称是：{key}")
                print(f"测试用例的数据是：{datas[key]}")
            else:
                print(f"{key}不是测试用例，不执行")



    def test_main(self):
        # self.load_data()
        self.handle_datas(datas=self.load_data())
