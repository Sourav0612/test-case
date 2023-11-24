import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from logging.handlers import RotatingFileHandler

from base.base_driver import BaseDriver
from utilities.utils import Utils


class swag_page(BaseDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver



    #Locators
    LOGIN_USERNAME = "//div[@id='login_credentials']"
    LOGIN_PASSWORD = "//div[@class='login_password']"
    USERNAME = "user-name"
    PASSWORD = "password"
    LOGIN_BUTTON = "//input[@id='login-button']"
    ITEM_1 = "//div[normalize-space()='Sauce Labs Backpack']"
    PRICE_1 = "//div[normalize-space()='$29.99']"
    DESCRIPTION_1 = "//div[normalize-space()='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.']"
    ITEM_2 = "//div[normalize-space()='Sauce Labs Bike Light']"
    PRICE_2 = "//div[normalize-space()='$9.99']"
    DESCRIPTION_2 = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]"
    ITEM_3 = "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    PRICE_3 = "//div[normalize-space()='$15.99']"
    DESCRIPTION_3 = "//div[normalize-space()='Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.']"
    ITEM_4 = "//div[normalize-space()='Sauce Labs Fleece Jacket']"
    PRICE_4 = "//div[normalize-space()='$49.99']"
    DESCRIPTION_4 = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]"
    ITEM_5 = "//div[normalize-space()='Sauce Labs Onesie']"
    PRICE_5 = "//div[normalize-space()='$7.99']"
    DESCRIPTION_5 = "//div[contains(text(),'Rib snap infant onesie for the junior automation e')]"
    ITEM_6 = "//div[normalize-space()='Test.allTheThings() T-Shirt (Red)']"
    PRICE_6 = "//div[normalize-space()='$15.99']"
    DESCRIPTION_6 = "//div[normalize-space()='This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.']"
    ADD_TO_CART_ITEM_1 = "add-to-cart-sauce-labs-backpack"
    BADGE = "//span[@class='shopping_cart_badge']"
    ADD_TO_CART_ITEM_2 = "add-to-cart-sauce-labs-bike-light"
    ADD_TO_CART_ITEM_3 = "add-to-cart-sauce-labs-bolt-t-shirt"
    ADD_TO_CART_ITEM_4 = "add-to-cart-sauce-labs-fleece-jacket"
    ADD_TO_CART_ITEM_5 = "add-to-cart-sauce-labs-onesie"
    ADD_TO_CART_ITEM_6 = "add-to-cart-test.allthethings()-t-shirt-(red)"
    REMOVE_FROM_CART_ITEM_1 = "remove-sauce-labs-backpack"
    REMOVE_FROM_CART_ITEM_2 = "remove-sauce-labs-bike-light"
    REMOVE_FROM_CART_ITEM_3 = "remove-sauce-labs-bolt-t-shirt"
    REMOVE_FROM_CART_ITEM_4 = "remove-sauce-labs-fleece-jacket"
    REMOVE_FROM_CART_ITEM_5 = "remove-sauce-labs-onesie"
    REMOVE_FROM_CART_ITEM_6 = "remove-test.allthethings()-t-shirt-(red)"
    MENU_BUTTON = "react-burger-menu-btn"
    BUTTON_1 = "//nav[@class='bm-item-list']//a[text()='All Items']"
    BUTTON_2 = "//nav[@class='bm-item-list']//a[text()='About']"
    BUTTON_3 = "//nav[@class='bm-item-list']//a[text()='Logout']"
    BUTTON_4 = "//nav[@class='bm-item-list']//a[text()='Reset App State']"
    CROSS_BUTTON = "react-burger-cross-btn"
    SORT_BAR = "//select[@class='product_sort_container']"













    #Login_Page
    def get_login_credentials(self):
        return self.locate_element(By.XPATH,self.LOGIN_USERNAME)

    def print_login_credentials(self):
        for i in self.get_login_credentials().text:
            print(i,end='')

    def get_login_password(self):
        return self.locate_element(By.XPATH,self.LOGIN_PASSWORD)
    def print_login_password(self):
        print("the password is :",self.get_login_password().text)

    def get_username(self):
        return self.locate_element(By.ID,self.USERNAME)
    def enter_username(self,username):
        self.get_username().send_keys(username)
    def get_password(self):
        return self.locate_element(By.ID,self.PASSWORD)
    def enter_password(self,password):
        self.get_password().send_keys(password)
    def get_login_button(self):
        return self.locate_element(By.XPATH,self.LOGIN_BUTTON)
    def login_button_click(self):
        self.get_login_button().click()
        time.sleep(2)

    #Only this method will be called in test_swag module

    def login_page_main(self):
        self.get_login_credentials()
        self.print_login_credentials()
        self.get_login_password()
        self.print_login_password()
        self.get_username()
        # You can add similar print functions for username, password, and login button if needed
        self.get_password()
        self.enter_username("standard_user")  # Replace with actual username
        self.enter_password("secret_sauce")  # Replace with actual password
        self.get_login_button()
        self.login_button_click()

    #Items_check
    def get_item_1(self):
        return self.locate_element(By.XPATH,self.ITEM_1)
    def print_item_1(self):
        print(self.get_item_1().text)

    def get_price_1(self):
        return self.locate_element(By.XPATH,self.PRICE_1)
    def print_price_1(self):
        print("the price of Sauce Labs Backpack is :",self.get_price_1().text)

    def get_description_1(self):
        return self.locate_element(By.XPATH,self.DESCRIPTION_1)
    def compare_description_1(self):
        desc_1 = Utils()
        desc_1.assert_item_text(self.get_description_1(),"carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
    def get_item_2(self):
        return self.locate_element(By.XPATH,self.ITEM_2)
    def print_item_2(self):
        print(self.get_item_2().text)

    def get_price_2(self):
        return self.locate_element(By.XPATH,self.PRICE_2)
    def print_price_2(self):
        print("the price of Sauce Labs Bike Light is : %s",self.get_price_2().text)

    def get_description_2(self):
        return self.locate_element(By.XPATH,self.DESCRIPTION_2)
    def compare_description_2(self):
        if "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included." in self.get_description_2().text:

            print("the description of product_2 is correct : A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.")


    def get_item_3(self):
        return self.locate_element(By.XPATH,self.ITEM_3)
    def print_item_3(self):
        print(self.get_item_3().text)

    def get_price_3(self):
        return self.locate_element(By.XPATH,self.PRICE_3)
    def print_price_3(self):
        print("the price of Sauce Labs Bolt T-Shirt is :",self.get_price_3().text)

    def get_description_3(self):
        return self.locate_element(By.XPATH,self.DESCRIPTION_3)
    def compare_description_3(self):
        desc_3 = Utils()
        desc_3.assert_item_text(self.get_description_3(),"Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.")

    def get_item_4(self):
        return self.locate_element(By.XPATH,self.ITEM_4)
    def print_item_4(self):
        print(self.get_item_4().text)

    def get_price_4(self):
        return self.locate_element(By.XPATH,self.PRICE_4)
    def print_price_4(self):
        print("the price of Sauce Labs Fleece Jacket is :",self.get_price_4().text)

    def get_description_4(self):
        return self.locate_element(By.XPATH,self.DESCRIPTION_4)
    def compare_description_4(self):
        desc_4 = Utils()
        desc_4.assert_item_text(self.get_description_4(),"It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.")

    def get_item_5(self):
        return self.locate_element(By.XPATH,self.ITEM_5)
    def print_item_5(self):
        print(self.get_item_5().text)

    def get_price_5(self):
        return self.locate_element(By.XPATH,self.PRICE_5)
    def print_price_5(self):
        print("the price of Sauce Labs Onesie is :",self.get_price_5().text)

    def get_description_5(self):
        return self.locate_element(By.XPATH,self.DESCRIPTION_5)
    def compare_description_5(self):
        desc_5 = Utils()
        desc_5.assert_item_text(self.get_description_5(),"Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.")

    def get_item_6(self):
        return self.locate_element(By.XPATH,self.ITEM_6)
    def print_item_6(self):
        print(self.get_item_6().text)

    def get_price_6(self):
        return self.locate_element(By.XPATH,self.PRICE_6)
    def print_price_6(self):
        print("the price of Test.allTheThings() T-Shirt (Red) is :",self.get_price_6().text)

    def get_description_6(self):
        return self.locate_element(By.XPATH,self.DESCRIPTION_6)
    def compare_description_6(self):
        desc_6 = Utils()
        desc_6.assert_item_text(self.get_description_6(),"This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.")

    #Only this method will be called in test_swag module

    def items_check_main(self):
        self.get_item_1()
        self.print_item_1()
        self.get_price_1()
        self.print_price_1()
        self.get_description_1()
        self.compare_description_1()
        self.get_item_2()
        self.print_item_2()
        self.get_price_2()
        self.print_price_2()
        self.get_description_2()
        self.compare_description_2()
        self.get_item_3()
        self.print_item_3()
        self.get_price_3()
        self.print_price_3()
        self.get_description_3()
        self.compare_description_3()
        self.get_item_4()
        self.print_item_4()
        self.get_price_4()
        self.print_price_4()
        self.get_description_4()
        self.compare_description_4()
        self.get_item_5()
        self.print_item_5()
        self.get_price_5()
        self.print_price_5()
        self.get_description_5()
        self.compare_description_5()
        self.get_item_6()
        self.print_item_6()
        self.get_price_6()
        self.print_price_6()
        self.get_description_6()
        self.compare_description_6()

    #Add_to_cart

    def get_add_to_cart_item_1(self):
        return self.locate_element(By.ID,self.ADD_TO_CART_ITEM_1)
    def click_add_to_cart_item_1(self):
        self.get_add_to_cart_item_1().click()
        time.sleep(2)
    def get_badge(self):
        return self.locate_element(By.XPATH,self.BADGE)
    def print_status_of_badge_1(self):
        print(self.get_badge().text,":item added")

    def get_add_to_cart_item_2(self):
        return self.locate_element(By.ID,self.ADD_TO_CART_ITEM_2)
    def click_add_to_cart_item_2(self):
        self.get_add_to_cart_item_2().click()
        time.sleep(2)

    def print_status_of_badge_2(self):
        print(self.get_badge().text,":items added")

    def get_add_to_cart_item_3(self):
        return self.locate_element(By.ID,self.ADD_TO_CART_ITEM_3)
    def click_add_to_cart_item_3(self):
        self.get_add_to_cart_item_3().click()
        time.sleep(2)
    def print_status_of_badge_3(self):
        print(self.get_badge().text,":items added")

    def get_add_to_cart_item_4(self):
        return self.locate_element(By.ID,self.ADD_TO_CART_ITEM_4)
    def click_add_to_cart_item_4(self):
        self.get_add_to_cart_item_4().click()
        time.sleep(2)
    def print_status_of_badge_4(self):
        print(self.get_badge().text,":items added ")

    def get_add_to_cart_item_5(self):
        return self.locate_element(By.ID,self.ADD_TO_CART_ITEM_5)
    def click_add_to_cart_item_5(self):
        self.get_add_to_cart_item_5().click()
        time.sleep(2)
    def print_status_of_badge_5(self):
        print(self.get_badge().text,":items added")

    def get_add_to_cart_item_6(self):
        return self.locate_element(By.ID,self.ADD_TO_CART_ITEM_6)
    def click_add_to_cart_item_6(self):
        self.get_add_to_cart_item_6().click()
        time.sleep(2)
    def print_status_of_badge_6(self):
        print(self.get_badge().text,":items added")


    #Only this method will be called in test_swag module

    def add_to_cart_main(self):
        self.get_add_to_cart_item_1()
        self.click_add_to_cart_item_1()
        self.get_badge()
        self.print_status_of_badge_1()
        self.get_add_to_cart_item_2()
        self.click_add_to_cart_item_2()
        self.print_status_of_badge_2()
        self.get_add_to_cart_item_3()
        self.click_add_to_cart_item_3()
        self.print_status_of_badge_3()
        self.get_add_to_cart_item_4()
        self.click_add_to_cart_item_4()
        self.print_status_of_badge_4()
        self.get_add_to_cart_item_5()
        self.click_add_to_cart_item_5()
        self.print_status_of_badge_5()
        self.get_add_to_cart_item_6()
        self.click_add_to_cart_item_6()
        self.print_status_of_badge_6()


    #Remove from cart

    def get_remove_item_1(self):
        return self.locate_element(By.ID,self.REMOVE_FROM_CART_ITEM_1)
    def click_remove_from_cart_item_1(self):
        self.get_remove_item_1().click()
        print(" Sauce labs backpack removed from cart ")

        time.sleep(2)
    def print_status_of_remove_badge_1(self):
        print("1:item removed:",self.get_badge().text,"items present in cart")

    def get_remove_item_2(self):
        return self.locate_element(By.ID,self.REMOVE_FROM_CART_ITEM_2)
    def click_remove_from_cart_item_2(self):
        self.get_remove_item_2().click()
        print("Sauce labs bike light removed from cart")

        time.sleep(2)
    def print_status_of_remove_badge_2(self):
        print("2:items removed:",self.get_badge().text,"items present in cart")

    def get_remove_item_3(self):
        return self.locate_element(By.ID,self.REMOVE_FROM_CART_ITEM_3)
    def click_remove_from_cart_item_3(self):
        self.get_remove_item_3().click()
        print("Sauce labs bolt t-shirt removed from cart")

        time.sleep(2)
    def print_status_of_remove_badge_3(self):
        print("3:items removed:",self.get_badge().text,"items present in cart")

    def get_remove_item_4(self):
        return self.locate_element(By.ID,self.REMOVE_FROM_CART_ITEM_4)
    def click_remove_from_cart_item_4(self):
        self.get_remove_item_4().click()
        print("Sauce labs fleece jacket removed from cart")

        time.sleep(2)
    def print_status_of_remove_badge_4(self):
        print("4:items removed:",self.get_badge().text,"items present in cart")

    def get_remove_item_5(self):
        return self.locate_element(By.ID,self.REMOVE_FROM_CART_ITEM_5)
    def click_remove_from_cart_item_5(self):
        self.get_remove_item_5().click()
        print("Sauce labs onesie removed from cart")

        time.sleep(2)
    def print_status_of_remove_badge_5(self):
        print("5:items removed:",self.get_badge().text,"items present in cart")

    def get_remove_item_6(self):
        return self.locate_element(By.ID,self.REMOVE_FROM_CART_ITEM_6)
    def click_remove_from_cart_item_6(self):
        self.get_remove_item_6().click()
        print("test.allthethings() t-shirt (red) removed from cart")

        time.sleep(2)
    def print_status_of_remove_badge_6(self):
        print("All items removed from cart")


    #Only this method will be called in test_swag module

    def remove_from_cart_main(self):
        self.get_remove_item_1()
        self.click_remove_from_cart_item_1()
        self.print_status_of_remove_badge_1()
        self.get_remove_item_2()
        self.click_remove_from_cart_item_2()
        self.print_status_of_remove_badge_2()
        self.get_remove_item_3()
        self.click_remove_from_cart_item_3()
        self.print_status_of_remove_badge_3()
        self.get_remove_item_4()
        self.click_remove_from_cart_item_4()
        self.print_status_of_remove_badge_4()
        self.get_remove_item_5()
        self.click_remove_from_cart_item_5()
        self.print_status_of_remove_badge_5()
        self.get_remove_item_6()
        self.click_remove_from_cart_item_6()
        self.print_status_of_remove_badge_6()


    #Menu options check
    def get_menu_button(self):
        return self.locate_element(By.ID,self.MENU_BUTTON)
    def menu_button_click(self):
        time.sleep(2)
        self.get_menu_button().click()
    def get_button_1(self):
        return self.locate_element(By.XPATH,self.BUTTON_1)
    def print_text_for_button_1(self):
        print(self.get_button_1().text)

    def get_button_2(self):
        return self.locate_element(By.XPATH,self.BUTTON_2)
    def print_text_for_button_2(self):
        print(self.get_button_2().text)

    def get_button_3(self):
        return self.locate_element(By.XPATH,self.BUTTON_3)
    def print_text_for_button_3(self):
        print(self.get_button_3().text)

    def get_button_4(self):
        return self.locate_element(By.XPATH,self.BUTTON_4)
    def print_text_for_button_4(self):
        print(self.get_button_4().text)

    def get_cross_button(self):
        return self.locate_element(By.ID,self.CROSS_BUTTON)
    def click_cross_button(self):
        self.get_cross_button().click()
        time.sleep(2)

    #Only this method will be called in test_swag module

    def menu_option_main(self):
        self.get_menu_button()
        self.menu_button_click()
        self.get_button_1()
        self.print_text_for_button_1()
        self.get_button_2()
        self.print_text_for_button_2()
        self.get_button_3()
        self.print_text_for_button_3()
        self.get_button_4()
        self.print_text_for_button_4()
        self.get_cross_button()
        self.click_cross_button()


    #Product sorting

    def get_sort_button(self):
        return self.locate_element(By.XPATH,self.SORT_BAR)
    def sorting(self):
        sort_bar = self.get_sort_button()
        sort_bar.click()
        time.sleep(2)

        # Loop through each option and select it
        for option_index in range(0, 4):
            sort_bar = self.get_sort_button()
            Select(sort_bar).select_by_index(option_index)
            time.sleep(2)

    #Only this method will be called in test_swag module

    def sorting_page_main(self):
        self.get_sort_button()
        self.sorting()



























