import allure

from screens.home_page_screen.authorization_window_screen import AuthorizationWindowScreen
from screens.home_page_screen.basket_screen import BasketScreen
from screens.home_page_screen.catalog_screen import CatalogScreen
from screens.home_page_screen.home_screen import HomeScreen
from screens.home_page_screen.personal_account_screen import PersonalAccountScreen


@allure.title('Login to user select product from catalog and checkout')
def test_checkout_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open authorization window on login tab'):
        home_screen.click_to_login()
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert login tab is displayed on authorization window'):
        authorization_screen.check_login_tab_is_displayed()
    with allure.step('Input user Name'):
        authorization_screen.input_login_tab_login_name_field("tesla")
    with allure.step('Input user Password'):
        authorization_screen.input_login_tab_password_field("Govai3223")
    with allure.step('Press Login button'):
        authorization_screen.click_login_tab_login_button()
    with allure.step('Navigate to Personal Account Screen'):
        personal_account_screen = PersonalAccountScreen(get_driver)
        personal_account_screen.check_personal_account_title('Личный кабинет')
    with allure.step('Assert basked selection item'):
        personal_account_screen.check_basked_selection_item_title('Корзина')
    with allure.step('Click on home page element'):
        home_screen.click_home_page_element()
    with allure.step('Assert catalog button on widget is displayed on home page'):
        home_screen.check_home_catalog_button_widget_is_displayed()
    with allure.step('Open Dnepr catalog screen'):
        home_screen.click_catalog_on_home_page()
        catalog_screen = CatalogScreen(get_driver)
        catalog_screen.click_dnepr_parts_catalog()
        catalog_screen.check_catalog_label_element('Запчасти Днепр МТ')
    with allure.step('Group list by text'):
        catalog_screen.select_groups_by_text()
    with allure.step('Add first item in list basket button'):
        catalog_screen.first_element_to_basked_button()
    with allure.step('Click basked on home page'):
        home_screen.check_basked_home_page_element()
        home_screen.click_basked_home_page_element()
    with allure.step('Assert basked element on basked screen'):
        basket_screen = BasketScreen(get_driver)
        basket_screen.check_basket_screen_locator_element()
    with allure.step('Press go to order button'):
        basket_screen.press_go_to_order_button()
    with allure.step('Press order button'):
        basket_screen.press_order_button()
