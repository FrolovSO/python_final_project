from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class RequestCallWindowScreenLocators:
    request_call_window_locator = (By.XPATH, '//*[@id="popup-window-titlebar-UniverseForm"]/span')
    close_button_locator = (By.XPATH, '//span[@class="popup-window-close-icon popup-window-titlebar-close-icon"]')
    name_field_locator = (
        By.XPATH, '//*[@class="startshop-forms-result-new-content intec-ui-form-field-content"]/input[@name="NAME"]')
    phone_field_locator = (
        By.XPATH, '//*[@class="startshop-forms-result-new-content intec-ui-form-field-content"]/input[@name="PHONE"]')
    agreements_checkbox_locator = (By.XPATH, '//*[@class="intec-ui-part-selector"]')
    request_button_locator = (
        By.XPATH, '//*[@class="intec-grid intec-grid-wrap intec-grid-i-5"]/div/button[@type="submit"]')
    reset_button_locator = (By.XPATH, '//*[@class="intec-grid intec-grid-wrap intec-grid-i-5"]/div/input')
    requirement_alert_name_field_locator = (By.XPATH,
                                            '//*[@class="startshop-forms-result-new-content intec-ui-form-field-content"]/input[@name="NAME"]/../../div')
    requirement_alert_phone_field_locator = (By.XPATH,
                                             '//*[@class="startshop-forms-result-new-content intec-ui-form-field-content"]/input[@name="PHONE"]/../../div')


class RequestCallWindowScreen(BasePage):

    def check_request_call_window_element(self):
        assert self.find_element(RequestCallWindowScreenLocators.request_call_window_locator).is_displayed()

    def check_request_call_window_closed(self):
        assert not self.find_element(RequestCallWindowScreenLocators.request_call_window_locator).is_displayed()

    def check_name_field_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.name_field_locator).is_displayed()

    def check_requirement_alert_name_field_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.requirement_alert_name_field_locator).is_displayed()

    def input_data_in_name_field(self, name):
        self.find_element(RequestCallWindowScreenLocators.name_field_locator).send_keys(name)

    def check_phone_field_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.phone_field_locator).is_displayed()

    def check_requirement_alert_phone_field_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.requirement_alert_phone_field_locator).is_displayed()

    def input_data_in_phone_field(self, number):
        self.find_element(RequestCallWindowScreenLocators.phone_field_locator).send_keys(number)

    def check_agreements_checkbox_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.agreements_checkbox_locator).is_displayed()

    def click_agreements_checkbox(self):
        self.find_element(RequestCallWindowScreenLocators.agreements_checkbox_locator).click()

    def check_request_button_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.request_button_locator).is_displayed()

    def check_request_button_is_disabled(self):
        assert not self.find_element(RequestCallWindowScreenLocators.request_button_locator).is_enabled()

    def press_request_button(self):
        self.find_element(RequestCallWindowScreenLocators.request_button_locator).click()

    def check_request_button_is_enable(self):
        assert self.find_element(RequestCallWindowScreenLocators.request_button_locator).is_enabled()

    def check_reset_button_is_displayed(self):
        assert self.find_element(RequestCallWindowScreenLocators.reset_button_locator).is_displayed()

    def press_reset_button(self):
        self.find_element(RequestCallWindowScreenLocators.reset_button_locator).click()

    def press_close_button(self):
        self.find_element(RequestCallWindowScreenLocators.close_button_locator).click()
