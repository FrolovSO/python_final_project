from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class PersonalAccountScreenLocators:
    personal_account_title_locator = (By.XPATH, '//h1[@id="pagetitle"]')
    basked_selection_item = (By.XPATH,
                             '//div[@class="sale-personal-section-items intec-grid intec-grid-wrap intec-grid-a-v-stretch intec-grid-i-8"]/div[3]//span[2]')


class PersonalAccountScreen(BasePage):

    def check_personal_account_title(self, value):
        label_text = self.get_text_from_element(PersonalAccountScreenLocators.personal_account_title_locator)
        assert label_text == value

    def check_basked_selection_item_title(self, value):
        label_text = self.get_text_from_element(PersonalAccountScreenLocators.basked_selection_item)
        assert label_text == value

    def click_basked_selection_item_title(self):
        self.find_element(PersonalAccountScreenLocators.basked_selection_item).click()
