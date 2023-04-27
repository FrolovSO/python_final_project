from selenium.webdriver.common.by import By

from control.base_page_demo import BasePage


class CatalogScreenLocators:
    catalog_label_locator = (By.XPATH, '//h1[@id="pagetitle"]')
    dnepr_catalog_locator = (By.XPATH,
                             '//div[@class="catalog-wrapper-2 intec-content-wrapper"]/div/div/div[9]/div/div/a[@href="/catalog/dnepr_mt/"]')
    icon_view_text_locator = (By.XPATH, '//i[@class="glyph-icon-view_text"]')
    icon_view_list_locator = (By.XPATH, '//i[@class="glyph-icon-view_list"]')
    icon_view_tile_locator = (By.XPATH, '//i[@class="glyph-icon-view_tile"]')
    list_sorting_locator = (By.XPATH, '//div[@class="catalog-panel-sort-icon"]')
    sorting_by_value_locator = (By.XPATH, '//div[@class="catalog-panel-sort-text"]')
    sorting_by_rating_list_locator = (By.XPATH, '//div[@data-role="catalog.panel.sortItems"]/div/div[2]/div/div')
    item_busked_button_locator = (By.XPATH, '//div[@data-id="1015"]//*[@class="catalog-section-item-purchase-buttons"]')
    first_element_from_list_locator = (By.XPATH, '//div[@class="catalog-section-item-background"]//div[@class="intec-ui-part-content"]')


class CatalogScreen(BasePage):
    def check_catalog_label_element(self, value):
        label_text = self.get_text_from_element(CatalogScreenLocators.catalog_label_locator)
        assert label_text == value

    def check_dnepr_parts_catalog(self):
        assert self.find_element(CatalogScreenLocators.dnepr_catalog_locator).is_displayed()

    def click_dnepr_parts_catalog(self):
        self.find_element(CatalogScreenLocators.dnepr_catalog_locator).click()

    def check_groups_by_text(self):
        assert self.find_element(CatalogScreenLocators.icon_view_text_locator).is_displayed()

    def select_groups_by_text(self):
        self.find_element(CatalogScreenLocators.icon_view_text_locator).click()

    def check_groups_by_list(self):
        assert self.find_element(CatalogScreenLocators.icon_view_list_locator).is_displayed()

    def check_groups_by_tile(self):
        assert self.find_element(CatalogScreenLocators.icon_view_tile_locator).is_displayed()

    def check_list_sorting(self):
        assert self.find_element(CatalogScreenLocators.icon_view_tile_locator).is_displayed()

    def click_list_sorting(self):
        self.find_element(CatalogScreenLocators.list_sorting_locator).click()

    def select_sorting_by_rating(self):
        self.find_element(CatalogScreenLocators.sorting_by_rating_list_locator).click()

    def check_sorting_by(self, sorting_by):
        sorting = self.get_text_from_element(CatalogScreenLocators.sorting_by_value_locator)
        assert sorting == sorting_by

    def check_item_basked_button(self):
        assert self.find_element(CatalogScreenLocators.item_busked_button_locator).is_displayed()

    def first_element_to_basked_button(self):
        self.click_element(CatalogScreenLocators.first_element_from_list_locator)
