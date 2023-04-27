import allure

from screens.home_page_screen.feedback_window_screen import FeedbackWindowScreen
from screens.home_page_screen.home_screen import HomeScreen


@allure.title('Open ask questions window')
def test_open_ask_questions_window_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert menu button is displayed on home page'):
        home_screen.check_menu_button_is_displayed()
    with allure.step('Open menu'):
        home_screen.click_menu_button()
    with allure.step('Assert ask questions button is displayed on menu'):
        home_screen.check_feedback_menu_button_is_displayed()
    with allure.step('Open ask questions window'):
        home_screen.click_feedback_menu_button()
    with allure.step('Assert ask questions window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_title('Задать вопрос')


@allure.title('Open and close ask questions window')
def test_open_and_close_ask_questions_window_2(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert menu button is displayed on home page'):
        home_screen.check_menu_button_is_displayed()
    with allure.step('Open menu'):
        home_screen.click_menu_button()
    with allure.step('Assert ask questions button is displayed on menu'):
        home_screen.check_feedback_menu_button_is_displayed()
    with allure.step('Open ask questions window'):
        home_screen.click_feedback_menu_button()
    with allure.step('Assert ask questions window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_title('Задать вопрос')
    with allure.step('Press Close window button'):
        feedback_window.press_close_button()
    with allure.step('Assert ask questions button is displayed on menu'):
        home_screen.check_feedback_menu_button_is_displayed()


@allure.title('Open ask questions and check enable buttons')
def test_open_and_close_ask_questions_window_3(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert menu button is displayed on home page'):
        home_screen.check_menu_button_is_displayed()
    with allure.step('Open menu'):
        home_screen.click_menu_button()
    with allure.step('Assert ask questions button is displayed on menu'):
        home_screen.check_feedback_menu_button_is_displayed()
    with allure.step('Open ask questions window'):
        home_screen.click_feedback_menu_button()
    with allure.step('Assert ask questions window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_title('Задать вопрос')
    with allure.step('Assert Sent button is disabled'):
        feedback_window.check_send_button_is_disabled()
    with allure.step('Put agreements checkbox in ask questions window'):
        feedback_window.click_agreements_checkbox()
    with allure.step('Assert Sent button is enable'):
        feedback_window.check_send_button_is_enable()


@allure.title('Open ask questions and enable buttons after reset')
def test__ask_questions_window_enable_buttons_after_reset_4(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert menu button is displayed on home page'):
        home_screen.check_menu_button_is_displayed()
    with allure.step('Open menu'):
        home_screen.click_menu_button()
    with allure.step('Assert ask questions button is displayed on menu'):
        home_screen.check_feedback_menu_button_is_displayed()
    with allure.step('Open ask questions window'):
        home_screen.click_feedback_menu_button()
    with allure.step('Assert ask questions window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_title('Задать вопрос')
    with allure.step('Assert Sent button is disabled'):
        feedback_window.check_send_button_is_disabled()
    with allure.step('Put agreements checkbox in ask questions window'):
        feedback_window.click_agreements_checkbox()
    with allure.step('Assert Sent button is enable'):
        feedback_window.check_send_button_is_enable()
    with allure.step('Press Reset button in ask questions window'):
        feedback_window.press_reset_button()
    with allure.step('Assert Sent button is disabled'):
        feedback_window.check_send_button_is_disabled()


@allure.title('Open ask questions and check requirement fields alerts')
def test_ask_questions_window_alerts_5(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert menu button is displayed on home page'):
        home_screen.check_menu_button_is_displayed()
    with allure.step('Open menu'):
        home_screen.click_menu_button()
    with allure.step('Assert ask questions button is displayed on menu'):
        home_screen.check_feedback_menu_button_is_displayed()
    with allure.step('Open ask questions window'):
        home_screen.click_feedback_menu_button()
    with allure.step('Assert ask questions window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_title('Задать вопрос')
    with allure.step('Put agreements checkbox in ask questions window'):
        feedback_window.click_agreements_checkbox()
    with allure.step('Assert Sent button is enable'):
        feedback_window.check_send_button_is_enable()
    with allure.step('Press Sent button in ask questions window'):
        feedback_window.press_send_button()
    with allure.step('Assert Name fild alert is disabled'):
        feedback_window.check_name_fild_alert('Поле должно быть заполнено')
    with allure.step('Assert Number fild alert is disabled'):
        feedback_window.check_number_fild_alert('Поле должно быть заполнено')
    with allure.step('Assert Question fild alert is disabled'):
        feedback_window.check_question_fild_alert('Поле должно быть заполнено')


@allure.title('Open and close feedback window')
def test_open_and_close_feedback_window_6(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert feedback button is displayed on home page'):
        home_screen.check_feedback_button_is_displayed()
    with allure.step('Open feedback window'):
        home_screen.click_feedback_button()
    with allure.step('Assert feedback window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_open()
        feedback_window.check_feedback_window_title('Обратная связь')
    with allure.step('Press Close window button'):
        feedback_window.press_close_button()
    with allure.step('Assert feedback button is displayed on home page'):
        home_screen.check_feedback_button_is_displayed()


@allure.title('Open and check feedback window fields')
def test_open_check_feedback_window_fields_7(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Check logo on home page'):
        home_screen.check_home_page_element()
    with allure.step('Assert feedback button is displayed on home page'):
        home_screen.check_feedback_button_is_displayed()
    with allure.step('Open feedback window'):
        home_screen.click_feedback_button()
    with allure.step('Assert feedback window is opened'):
        feedback_window = FeedbackWindowScreen(get_driver)
        feedback_window.check_feedback_window_open()
        feedback_window.check_feedback_window_title('Обратная связь')
    with allure.step('Set Name in feedback window'):
        feedback_window.set_input_name('Name')

