from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class HomeScreenLocators:
    label_locator = (By.XPATH, '//img[@alt="MVPARTS.BY"]')
    basked_locator = (By.XPATH, '//*[@class="sale-basket-small-tab-icon glyph-icon-cart"]/../../../a[@href="/personal/basket/"]')
    catalog_locator = (By.XPATH, '//a[@href="/catalog/"]/div')
    about_company_locator = (By.XPATH, '//a[@href="/company/"]/div')
    payment_and_delivery_locator = (By.XPATH, '//a[@href="/help/client/"]/div')
    contacts_locator = (By.XPATH, '//a[@href="/contacts/"]/div')
    search_icon_locator = (By.XPATH, '//i[@class="glyph-icon-loop"]')
    login_button_locator = (By.XPATH, '//*[@class="widget-authorization-panel"]/div[@data-action="login"]')
    logout_button_locator = (By.XPATH, '//div[@class="widget-authorization-panel"]/a[2]/div/div[@class="widget-panel-button-text intec-grid-item-auto"]')
    request_a_call_locator = (By.XPATH, '//div[@data-block="phone"]/div[2]/div[@data-action="forms.call.open"]')
    catalog_button_widget_locator = (By.XPATH, '//a[@href="https://mvparts.by/catalog/"]')
    popular_categories_locator = (By.XPATH, '//div[@class="widget-title-container intec-grid-item"]/div[text()="Популярные категории"]')
    popular_goods_locator = (By.XPATH, '//div[@class="widget-title-container intec-grid-item"]/div[text()="Популярные товары"]')
    button_up_locator = (By.XPATH, '//*[@stroke-linejoin="round"]/../../../div[@class="widget-button-wrapper"]')
    feedback_widget_locator = (By.XPATH, '//div[@class="widget-form-name"]')
    feedback_button_locator = (By.XPATH, '//div[@class="widget-form-button intec-cl-background intec-cl-background-light-hover intec-ui intec-ui-control-button intec-ui-mod-round-2 intec-ui-scheme-current"]')
    menu_button_locator = (By.XPATH, '//div[@class="widget-menu-popup"]/div/div')
    feedback_menu_button_locator = (By.XPATH, '//span[@class="intec-ui intec-ui-control-button intec-ui-mod-round-2 intec-ui-mod-transparent intec-ui-scheme-current menu-content-feedback"]')
    block_locator = [By.XPATH, '//div[@class="widget-view widget-view-fixed"][@style="display: block; top: 0px;"]']

class HomeScreen(BasePage):

    def check_home_page_element(self):
        assert self.find_element(HomeScreenLocators.label_locator).is_displayed()

    def click_home_page_element(self):
        self.find_element(HomeScreenLocators.label_locator).click()

    def click_to_login(self):
        self.click_element(HomeScreenLocators.login_button_locator)

    def click_to_logout(self):
        self.click_element(HomeScreenLocators.logout_button_locator)

    def check_basked_home_page_element(self):
        assert self.find_element(HomeScreenLocators.basked_locator).is_displayed()

    def click_basked_home_page_element(self):
        self.find_element(HomeScreenLocators.basked_locator).click()

    def click_to_request_a_call(self):
        self.click_element(HomeScreenLocators.request_a_call_locator)

    def check_home_page_catalog(self):
        assert self.find_element(HomeScreenLocators.catalog_locator).is_displayed()

    def click_catalog_on_home_page(self):
        self.find_element(HomeScreenLocators.catalog_locator).click()

    def check_home_page_about_company(self):
        assert self.find_element(HomeScreenLocators.about_company_locator).is_displayed()

    def check_home_page_payment_and_delivery(self):
        assert self.find_element(HomeScreenLocators.payment_and_delivery_locator).is_displayed()

    def check_home_page_contacts(self):
        assert self.find_element(HomeScreenLocators.contacts_locator).is_displayed()

    def check_home_search_is_displayed(self):
        assert self.find_element(HomeScreenLocators.search_icon_locator).is_displayed()

    def check_home_login_button_is_displayed(self):
        assert self.find_element(HomeScreenLocators.login_button_locator).is_displayed()

    def check_home_logout_button_is_displayed(self):
        assert self.find_element(HomeScreenLocators.logout_button_locator).is_displayed()

    def check_home_request_a_call_is_displayed(self):
        assert self.find_element(HomeScreenLocators.request_a_call_locator).is_displayed()

    def check_home_catalog_button_widget_is_displayed(self):
        assert self.find_element(HomeScreenLocators.catalog_button_widget_locator).is_displayed()

    def check_home_popular_categories_is_displayed(self):
        assert self.find_element(HomeScreenLocators.popular_categories_locator).is_displayed()

    def check_home_popular_goods_is_displayed(self):
        assert self.find_element(HomeScreenLocators.popular_goods_locator).is_displayed()

    def check_feedback_button_is_displayed(self):
        self.click_element(HomeScreenLocators.feedback_widget_locator)
        assert self.find_element(HomeScreenLocators.feedback_button_locator).is_displayed()

    def click_feedback_button(self):
        self.click_element(HomeScreenLocators.feedback_button_locator)

    def check_menu_button_is_displayed(self):
        self.scroll_by_pixel()
        self.find_element(HomeScreenLocators.block_locator).is_displayed()
        assert self.find_element(HomeScreenLocators.menu_button_locator).is_displayed()

    def click_menu_button(self):
        self.click_element(HomeScreenLocators.menu_button_locator)

    def check_feedback_menu_button_is_displayed(self):
        assert self.find_element(HomeScreenLocators.feedback_menu_button_locator).is_displayed()

    def click_feedback_menu_button(self):
        self.click_element(HomeScreenLocators.feedback_menu_button_locator)
