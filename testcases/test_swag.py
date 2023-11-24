import pytest


from pages.swag_page import swag_page


@pytest.mark.usefixtures("setup")
class Testswag():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = swag_page(self.driver)


    def testlogin(self):
        self.lp.login_page_main()



    def testitems(self):
        self.lp.items_check_main()






    def testadd_to_cart(self):
        self.lp.add_to_cart_main()





    def testremove_cart(self):
        self.lp.remove_from_cart_main()




    def testmenu_button(self):
        self.lp.page_scroll()
        self.lp.menu_option_main()





    def testproduct_sorting(self):
        self.lp.sorting_page_main()

































