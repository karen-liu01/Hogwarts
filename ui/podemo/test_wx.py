from ui.podemo.index_page import IndexPage


class TestWX:
    def setup(self):
        self.index = IndexPage()


    def teardown(self):
        pass

    def test_register(self):
        # self.index.goto_register().register()
        assert  self.index.goto_login().goto_register().register()