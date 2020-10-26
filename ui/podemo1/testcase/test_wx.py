from ui.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()


    def test_addmember(self):
        assert self.main.goto_addmember().add_member()