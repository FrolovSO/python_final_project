import allure

from screens.home_page_screen.home_screen import HomeScreen
from screens.home_page_screen.request_a_call_window_screen import RequestCallWindowScreen


@allure.title('Open request call window and assert is window on home page')
def test_open_request_call_window_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()


@allure.title('Open and close request call window')
def test_open_and_close_request_call_window_2(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Press Close window button'):
        request_call_window_screen.press_close_button()
    with allure.step('Assert closed window'):
        request_call_window_screen.check_request_call_window_closed()


@allure.title('Open request call window on home page and check contains this window')
def test_check_contain_request_call_window_3(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Assert request call window is contains Name fild'):
        request_call_window_screen.check_name_field_is_displayed()
    with allure.step('Assert request call window is contains Phone Number fild'):
        request_call_window_screen.check_phone_field_is_displayed()
    with allure.step('Assert request call window is contains Agreements checkbox'):
        request_call_window_screen.check_agreements_checkbox_is_displayed()
    with allure.step('Assert request call window is contains Request button'):
        request_call_window_screen.check_request_button_is_displayed()
    with allure.step('Assert request call window is contains Reset button'):
        request_call_window_screen.check_reset_button_is_displayed()


@allure.title('Button Request is disabled by default and enable after put Agreements checkbox')
def test_enable_disable_request_button_4(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Assert Request button is disabled'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_disabled()
    with allure.step('Fill the Agreements checkbox'):
        request_call_window_screen.check_agreements_checkbox_is_displayed()
        request_call_window_screen.click_agreements_checkbox()
    with allure.step('Assert Request button is enable'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_enable()


@allure.title('Request a call check requirement fields alerts')
def test_requirement_fields_alerts_5(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Enable Request button'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_disabled()
        request_call_window_screen.click_agreements_checkbox()
        request_call_window_screen.check_request_button_is_enable()
    with allure.step('Press Request button'):
        request_call_window_screen.press_request_button()
    with allure.step('Assert requirement alerts for Name'):
        request_call_window_screen.check_requirement_alert_name_field_is_displayed()
    with allure.step('Assert requirement alerts for Phone'):
        request_call_window_screen.check_requirement_alert_phone_field_is_displayed()


@allure.title('Request a call without a Name')
def test_request_call_without_name_6(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Enable Request button'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_disabled()
        request_call_window_screen.click_agreements_checkbox()
        request_call_window_screen.check_request_button_is_enable()
    with allure.step('Input name in name field'):
        request_call_window_screen.input_data_in_name_field("Test")
    with allure.step('Press Request button'):
        request_call_window_screen.press_request_button()
    with allure.step('Assert requirement alerts for Phone'):
        request_call_window_screen.check_requirement_alert_phone_field_is_displayed()


@allure.title('Request a call without a Phone')
def test_request_call_without_phone_7(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Enable Request button'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_disabled()
        request_call_window_screen.click_agreements_checkbox()
        request_call_window_screen.check_request_button_is_enable()
    with allure.step('Input name in phone field'):
        request_call_window_screen.input_data_in_phone_field("123456789")
    with allure.step('Press Request button'):
        request_call_window_screen.press_request_button()
    with allure.step('Assert requirement alerts for Name'):
        request_call_window_screen.check_requirement_alert_name_field_is_displayed()


@allure.title('Request a call check reset button')
def test_request_call_reset_button_8(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
        home_screen.check_home_page_element()
    with allure.step('Open request a call window'):
        home_screen.click_to_request_a_call()
    with allure.step('Assert request call window is open on home page'):
        request_call_window_screen = RequestCallWindowScreen(get_driver)
        request_call_window_screen.check_request_call_window_element()
    with allure.step('Enable Request button'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_disabled()
        request_call_window_screen.click_agreements_checkbox()
        request_call_window_screen.check_request_button_is_enable()
    with allure.step('Input name in name field'):
        request_call_window_screen.input_data_in_name_field("Test")
    with allure.step('Input name in phone field'):
        request_call_window_screen.input_data_in_phone_field("123456789")
    with allure.step('Press Reset button'):
        request_call_window_screen.press_reset_button()
    with allure.step('Assert Request button is disabled'):
        request_call_window_screen.check_request_button_is_displayed()
        request_call_window_screen.check_request_button_is_disabled()
