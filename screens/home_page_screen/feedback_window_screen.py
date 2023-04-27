from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class FeedbackWindowScreenLocators:
    feedback_window_locator = (By.XPATH, '//*[@id="popup-window-titlebar-UniverseForm"]/span')
    close_button_locator = (By.XPATH, '//span[@class="popup-window-close-icon popup-window-titlebar-close-icon"]')
    window_locator = (By.XPATH, '//div[@id="UniverseForm"]')
    input_name_locator = (By.XPATH, '//div[@class="startshop-forms-result-new-content intec-ui-form-field-content"]/input[@name="NAME"]')
    agreements_checkbox_locator = (By.XPATH, '//div[@class="startshop-forms-result-new-consent"]//span[@class="intec-ui-part-selector"]')
    reset_button_locator = (By.XPATH, '//input[@class="startshop-forms-result-new-reset-button intec-ui intec-ui-control-button intec-ui-mod-round-2 intec-ui-mod-transparent intec-ui-size-1"]')
    send_button_locator = (By.XPATH, '//button[@class="startshop-forms-result-new-submit-button intec-ui intec-ui-control-button intec-ui-mod-round-2 intec-ui-scheme-current intec-ui-size-1"]')
    name_fild_alert_locator = (By.XPATH, '//input[@name="NAME"]/../../div[@class="startshop-forms-result-new-message-error"]')
    question_fild_alert_locator = (By.XPATH, '//input[@name="QUESTION"]/../../div[@class="startshop-forms-result-new-message-error"]')
    number_fild_alert_locator = (By.XPATH, '//input[@name="PHONE"]/../../div[@class="startshop-forms-result-new-message-error"]')


class FeedbackWindowScreen(BasePage):

    def check_feedback_window_title(self, value):
        label_text = self.get_text_from_element(FeedbackWindowScreenLocators.feedback_window_locator)
        assert label_text == value

    def check_feedback_window_open(self):
        assert self.find_element(FeedbackWindowScreenLocators.window_locator).is_displayed()

    def press_close_button(self):
        self.find_element(FeedbackWindowScreenLocators.close_button_locator).click()

    def set_input_name(self, name):
        self.find_element(FeedbackWindowScreenLocators.input_name_locator).send_keys(name)

    def click_agreements_checkbox(self):
        self.click_element(FeedbackWindowScreenLocators.agreements_checkbox_locator)

    def check_send_button_is_disabled(self):
        assert not self.find_element(FeedbackWindowScreenLocators.send_button_locator).is_enabled()

    def press_send_button(self):
        self.find_element(FeedbackWindowScreenLocators.send_button_locator).click()

    def check_send_button_is_enable(self):
        assert self.find_element(FeedbackWindowScreenLocators.send_button_locator).is_enabled()

    def press_reset_button(self):
        self.find_element(FeedbackWindowScreenLocators.reset_button_locator).click()

    def check_name_fild_alert(self, alert):
        alert_text = self.get_text_from_element(FeedbackWindowScreenLocators.name_fild_alert_locator)
        assert alert_text == alert

    def check_number_fild_alert(self, alert):
        alert_text = self.get_text_from_element(FeedbackWindowScreenLocators.number_fild_alert_locator)
        assert alert_text == alert

    def check_question_fild_alert(self, alert):
        alert_text = self.get_text_from_element(FeedbackWindowScreenLocators.question_fild_alert_locator)
        assert alert_text == alert
