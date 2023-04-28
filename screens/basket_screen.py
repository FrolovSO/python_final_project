from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class BasketScreenLocators:
    basket_screen_locator = (By.XPATH, '//*[@id="pagetitle"]')
    catalog_empty_basket_locator = (By.XPATH, '//*[@class="startshop-basket-basket-empty-description"]/../a')
    go_to_order_button_locator = (By.XPATH, '//div[@class="startshop-basket-basket-buttons"]//a')
    order_button_locator = (By.XPATH, '//button[@class="intec-ui intec-ui-control-button intec-ui-scheme-current intec-ui-mod-round-2 intec-ui-size-5"]')


class BasketScreen(BasePage):

    def check_basket_screen_locator_element(self):
        assert self.find_element(BasketScreenLocators.basket_screen_locator).is_displayed()

    def check_catalog_empty_basket_button_element(self):
        assert self.find_element(BasketScreenLocators.catalog_empty_basket_locator).is_displayed()

    def press_go_to_order_button(self):
        self.click_element(BasketScreenLocators.go_to_order_button_locator)

    def press_order_button(self):
        self.click_element(BasketScreenLocators.order_button_locator)
