import allure

from screens.home_page_screen.authorization_window_screen import AuthorizationWindowScreen
from screens.home_page_screen.home_screen import HomeScreen


@allure.title('Open authorization and assert is window on home page')
def test_open_authorisation_window_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
        home_screen.click_to_login()
    with allure.step('Assert authorization window is open on home page'):
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()


@allure.title('Open authorization window and check registration tab is displayed on home page')
def test_check_registration_tab_2(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
        home_screen.click_to_login()
    with allure.step('Assert authorization window is open on home page'):
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert registration tab is displayed on authorization window'):
        authorization_screen.check_registration_tab_is_displayed()


@allure.title('Open authorization window and check registration tab contains on home page')
def test_check_authorisation_window_registration_tab_contains_3(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
        home_screen.click_to_login()
    with allure.step('Assert authorization window is open on home page'):
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert registration tab is displayed on authorization window'):
        authorization_screen.check_registration_tab_is_displayed()
        authorization_screen.click_on_registration_tab()
    with allure.step('Assert registration tab is contains Login Name fild'):
        authorization_screen.check_login_name_field_is_displayed()
    with allure.step('Assert registration tab is contains Email fild'):
        authorization_screen.check_email_field_is_displayed()
    with allure.step('Assert registration tab is contains Password fild'):
        authorization_screen.check_password_field_is_displayed()
    with allure.step('Assert registration tab is contains Password again fild'):
        authorization_screen.check_password_second_field_is_displayed()
    with allure.step('Assert registration tab is contains Agreements checkbox'):
        authorization_screen.check_agreements_checkbox_is_displayed()
    with allure.step('Assert registration tab is contains Create Account button'):
        authorization_screen.check_create_account_button_is_displayed()
    with allure.step('Assert registration tab is contains Login button'):
        authorization_screen.check_login_button_is_displayed()


@allure.title('Open login window and check login tab is displayed on home page')
def test_check_login_tab_4(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
        home_screen.click_to_login()
    with allure.step('Assert authorization window is open on home page'):
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert login tab is displayed on authorization window'):
        authorization_screen.check_login_tab_is_displayed()


@allure.title('Open authorization window and check login tab contains on home page')
def test_check_authorisation_window_login_tab_contains_5(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
        home_screen.click_to_login()
    with allure.step('Assert authorization window is open on home page'):
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert login tab is displayed on authorization window'):
        authorization_screen.check_login_tab_is_displayed()
        authorization_screen.click_on_registration_tab()
        authorization_screen.click_on_login_tab()
    with allure.step('Assert login tab is contains Login Name fild'):
        authorization_screen.login_tab_login_name_field_is_displayed()
    with allure.step('Assert login tab is contains Password fild'):
        authorization_screen.login_tab_password_field_is_displayed()
    with allure.step('Assert login tab is contains remember switch'):
        authorization_screen.login_tab_remember_switch_is_displayed()
    with allure.step('Assert login tab is contains forgot password linc'):
        authorization_screen.login_tab_forgot_password_link_is_displayed()
    with allure.step('Assert login tab is contains Login button'):
        authorization_screen.login_tab_login_button_is_displayed()


@allure.title('Open authorization window registration tab and press Create Account button')
def test_check_registration_tab_press_create_account_6(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
        home_screen.click_to_login()
    with allure.step('Assert authorization window is open on home page'):
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert registration tab is displayed on authorization window'):
        authorization_screen.check_registration_tab_is_displayed()
        authorization_screen.click_on_registration_tab()
    with allure.step('Press Create Account button'):
        authorization_screen.click_create_account_button()
    with allure.step('Assert registration tab is contains Login Name fild alert is displayed'):
        authorization_screen.check_login_name_field_alert_is_displayed()
    with allure.step('Assert registration tab is contains Email fild alert is displayed'):
        authorization_screen.check_email_field_alert_is_displayed()
    with allure.step('Assert registration tab is contains Password fild alert is displayed'):
        authorization_screen.check_password_field_alert_is_displayed()
    with allure.step('Assert registration tab is contains Password again fild alert is displayed'):
        authorization_screen.check_password_second_field_alert_is_displayed()


@allure.title('Open authorization window and press login button on login tab')
def test_check_login_tab_press_login_7(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open authorization window on login tab'):
        home_screen.click_to_login()
        authorization_screen = AuthorizationWindowScreen(get_driver)
        authorization_screen.check_authorization_window_element()
    with allure.step('Assert login tab is displayed on authorization window'):
        authorization_screen.check_login_tab_is_displayed()
    with allure.step('Press Login button'):
        authorization_screen.click_login_tab_login_button()
    with allure.step('Assert navigation on authorization screen'):
        authorization_screen.check_authorization_screen_logo()
    with allure.step('Assert wrong password or login name alert'):
        authorization_screen.check_wrong_password_alert()
