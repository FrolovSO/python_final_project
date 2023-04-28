from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class AuthorizationWindowScreenLocators:
    authorization_window_locator = (By.XPATH, '//div[@id="popup-window-titlebar-UniverseComponent"]/span')
    registration_tab_locator = (
    By.XPATH, '//a[@href="#i-0-bitrix-system-auth-form-template-2-iIjGFB3HxHmm_tab_registration"]')
    login_tab_locator = (By.XPATH, '//a[@href="#i-0-bitrix-system-auth-form-template-2-iIjGFB3HxHmm_tab_auth"]')
    login_name_field_locator = (By.XPATH, '//input[@id="REGISTER_LOGIN_POPUP2"]')
    email_field_locator = (By.XPATH, '//input[@id="REGISTER_EMAIL_POPUP2"]')
    password_field_locator = (By.XPATH, '//input[@id="REGISTER_PASSWORD_POPUP2"]')
    password_second_field_locator = (By.XPATH, '//input[@id="REGISTER_CONFIRM_PASSWORD_POPUP2"]')
    agreements_checkbox_locator = (By.XPATH, '//a[@href="/company/consent/"]/../../input/../span[2]')
    create_account_button_locator = (By.XPATH, '//*[@value="Создать аккаунт"]')
    login_button_locator = (By.XPATH, '//*[@value="Создать аккаунт"]/../../div[2]/div[2]/a')
    login_tab_login_name_field_locator = (By.XPATH, '//*[@class="intec-ui-form-field-content"]/input')
    login_tab_password_field_locator = (By.XPATH, '//input[@id="USER_PASSWORD_2"]')
    login_tab_remember_switch_locator = (By.XPATH, '//*[@class="intec-ui intec-ui-control-switch intec-ui-scheme-current intec-ui-size-3"]')
    login_tab_forgot_password_link_locator = (By.XPATH, '//a[@href="/personal/profile/?forgot_password=yes"]')
    login_tab_login_button_locator = (By.XPATH, '//*[@class="system-auth-authorize-buttons"]/input')
    login_name_field_alert_locator = (By.XPATH, '//*[@class="errortext"]')
    email_field_alert_locator = (By.XPATH, '//*[@class="errortext"]')
    password_field_alert_locator = (By.XPATH, '//*[@class="errortext"]')
    password_second_field_alert_locator = (By.XPATH, '//*[@class="errortext"]')
    authorization_screen_logo_locator = (By.XPATH, '//h1[@id="pagetitle"]')
    wrong_password_alert_locator = (By.XPATH, '//div[@class="intec-ui intec-ui-control-alert intec-ui-scheme-red intec-ui-m-b-20"]')


class AuthorizationWindowScreen(BasePage):

    def check_authorization_window_element(self):
        assert self.find_element(AuthorizationWindowScreenLocators.authorization_window_locator).is_displayed()

    def check_registration_tab_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.registration_tab_locator).is_displayed()

    def click_on_registration_tab(self):
        self.find_element(AuthorizationWindowScreenLocators.registration_tab_locator).click()

    def check_login_tab_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_tab_locator).is_displayed()

    def click_on_login_tab(self):
        self.find_element(AuthorizationWindowScreenLocators.login_tab_locator).click()

    def check_login_name_field_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_name_field_locator).is_displayed()

    def check_login_name_field_alert_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_name_field_alert_locator).is_displayed()

    def check_email_field_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.email_field_locator).is_displayed()

    def check_email_field_alert_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.email_field_alert_locator).is_displayed()

    def check_password_field_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.password_field_locator).is_displayed()

    def check_password_field_alert_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.password_field_alert_locator).is_displayed()

    def check_password_second_field_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.password_second_field_locator).is_displayed()

    def check_password_second_field_alert_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.password_second_field_alert_locator).is_displayed()

    def check_agreements_checkbox_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.agreements_checkbox_locator).is_displayed()

    def check_create_account_button_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.create_account_button_locator).is_displayed()

    def click_create_account_button(self):
        self.find_element(AuthorizationWindowScreenLocators.create_account_button_locator).click()

    def check_login_button_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_button_locator).is_displayed()

    def login_tab_login_name_field_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_tab_login_name_field_locator).is_displayed()

    def input_login_tab_login_name_field(self, name):
        self.find_element(AuthorizationWindowScreenLocators.login_tab_login_name_field_locator).send_keys(name)

    def login_tab_password_field_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_tab_password_field_locator).is_displayed()

    def input_login_tab_password_field(self, password):
        self.find_element(AuthorizationWindowScreenLocators.login_tab_password_field_locator).send_keys(password)

    def login_tab_remember_switch_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_tab_remember_switch_locator).is_displayed()

    def login_tab_forgot_password_link_is_displayed(self):
        assert self.find_element(
            AuthorizationWindowScreenLocators.login_tab_forgot_password_link_locator).is_displayed()

    def login_tab_login_button_is_displayed(self):
        assert self.find_element(AuthorizationWindowScreenLocators.login_tab_login_button_locator).is_displayed()

    def click_login_tab_login_button(self):
        self.find_element(AuthorizationWindowScreenLocators.login_tab_login_button_locator).click()

    def check_authorization_screen_logo(self):
        assert self.find_element(AuthorizationWindowScreenLocators.authorization_screen_logo_locator).is_displayed()

    def check_wrong_password_alert(self):
        assert self.find_element(AuthorizationWindowScreenLocators.wrong_password_alert_locator).is_displayed()
