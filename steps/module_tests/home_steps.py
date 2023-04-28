import allure

from screens.home_screen import HomeScreen


@allure.title('Open web page')
def test_open_web_page_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Click to logo on home page'):
        home_screen.click_to_login()
    with allure.step('Assert the logo on home page'):
        home_screen.check_home_page_element()


@allure.title('Open web page and check Basket on home page')
def test_check_basked_on_home_page_2(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Click basked on home page'):
        home_screen.check_basked_home_page_element()


@allure.title('Open home web page and verify tabs on page')
def test_home_page_tab_contains_3(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert catalog tad is displayed on home page'):
        home_screen.check_home_page_catalog()
    with allure.step('Assert about company tad is displayed on home page'):
        home_screen.check_home_page_about_company()
    with allure.step('Assert payment and delivery tad is displayed on home page'):
        home_screen.check_home_page_payment_and_delivery()
    with allure.step('Assert contacts tad is displayed on home page'):
        home_screen.check_home_page_contacts()


@allure.title('Open home web page and check displayed search')
def test_search_is_displayed_4(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert search is displayed on home page'):
        home_screen.check_home_search_is_displayed()


@allure.title('Open home web page and check displayed login button')
def test_login_is_displayed_5(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert login button is displayed on home page'):
        home_screen.check_home_login_button_is_displayed()


@allure.title('Open home web page and check displayed request a call')
def test_request_a_call_is_displayed_6(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert request a call link is displayed on home page'):
        home_screen.check_home_request_a_call_is_displayed()


@allure.title('Open home web page and check displayed catalog on widget')
def test_go_to_catalog_on_widget_7(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert catalog button on widget is displayed on home page'):
        home_screen.check_home_catalog_button_widget_is_displayed()


@allure.title('Open home web page and check displayed popular categories')
def test_popular_categories_is_displayed_8(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert popular categories is displayed on home page'):
        home_screen.check_home_popular_categories_is_displayed()


@allure.title('Open home web page and check displayed popular goods on home page')
def test_popular_goods_is_displayed_9(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert popular categories is displayed on home page'):
        home_screen.check_home_popular_goods_is_displayed()


@allure.title('Open home web page and check feedback button')
def test_feedback_button_is_displayed_10(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert feedback button is displayed on home page'):
        home_screen.check_feedback_button_is_displayed()


@allure.title('Open menu on home page')
def test_open_menu_on_home_page_11(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert menu button is displayed on home page'):
        home_screen.check_menu_button_is_displayed()
