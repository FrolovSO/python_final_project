import allure

from screens.basket_screen import BasketScreen
from screens.home_screen import HomeScreen


@allure.title('Open basket screen and assert screen logo')
def test_open_basket_screen_assert_logo_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Click basked on home page'):
        home_screen.check_basked_home_page_element()
        home_screen.click_basked_home_page_element()
    with allure.step('Assert basked element on basked screen'):
        basket_screen = BasketScreen(get_driver)
        basket_screen.check_basket_screen_locator_element()


@allure.title('Open basket screen and assert empty screen elements')
def test_open_basket_screen_assert_elements_2(get_driver):
    with allure.step('Navigate to basked screen'):
        home_screen = HomeScreen(get_driver)
        home_screen.click_basked_home_page_element()
        basket_screen = BasketScreen(get_driver)
        basket_screen.check_basket_screen_locator_element()
    with allure.step('Assert empty basked elements on basked screen'):
        basket_screen.check_catalog_empty_basket_button_element()
