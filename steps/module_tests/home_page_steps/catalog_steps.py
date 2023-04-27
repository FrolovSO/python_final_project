import allure

from screens.home_page_screen.catalog_screen import CatalogScreen
from screens.home_page_screen.home_screen import HomeScreen


@allure.title('Navigate to catalog screen')
def test_open_catalog_screen_1(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Open catalog screen'):
        home_screen.check_home_page_element()
        home_screen.check_home_page_catalog()
        home_screen.click_catalog_on_home_page()
    with allure.step('Assert catalog label is displayed'):
        catalog_screen = CatalogScreen(get_driver)
        catalog_screen.check_catalog_label_element('Каталог запчастей, расходников и аксессуаров для мотоциклов')


@allure.title('Open catalog for Dnepr parts')
def test_open_dnepar_parts_catalog_2(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Open catalog screen'):
        home_screen.check_home_page_element()
        home_screen.check_home_page_catalog()
        home_screen.click_catalog_on_home_page()
    with allure.step('Assert catalog label is displayed'):
        catalog_screen = CatalogScreen(get_driver)
        catalog_screen.check_catalog_label_element('Каталог запчастей, расходников и аксессуаров для мотоциклов')
    with allure.step('Assert Dnepr catalog is displayed'):
        catalog_screen.check_dnepr_parts_catalog()
        catalog_screen.click_dnepr_parts_catalog()
    with allure.step('Assert Dnepr catalog screen'):
        catalog_screen.check_catalog_label_element('Запчасти Днепр МТ')


@allure.title('Verify catalog panel view for Dnepr parts')
def test_dnepar_parts_catalog_panel_view_3(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Open Dnepr catalog screen'):
        home_screen.click_catalog_on_home_page()
        catalog_screen = CatalogScreen(get_driver)
        catalog_screen.click_dnepr_parts_catalog()
        catalog_screen.check_catalog_label_element('Запчасти Днепр МТ')
    with allure.step('Assert groups icon view panels'):
        catalog_screen.check_groups_by_text()
        catalog_screen.check_groups_by_list()
        catalog_screen.check_groups_by_tile()


@allure.title('Verify catalog panel sorting for Dnepr parts')
def test_dnepar_parts_catalog_panel_sorting_4(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Open Dnepr catalog screen'):
        home_screen.click_catalog_on_home_page()
        catalog_screen = CatalogScreen(get_driver)
        catalog_screen.click_dnepr_parts_catalog()
        catalog_screen.check_catalog_label_element('Запчасти Днепр МТ')
    with allure.step('Assert icon sorting view panels'):
        catalog_screen.check_list_sorting()
    with allure.step('Sorting by rating'):
        catalog_screen.click_list_sorting()
        catalog_screen.select_sorting_by_rating()
    with allure.step('Assert sorting by'):
        catalog_screen.check_sorting_by('По рейтингу')


@allure.title('Verify catalog item contain basket button for Dnepr parts')
def test_dnepar_parts_catalog_panel_item_basked_button_5(get_driver):
    with allure.step('Navigate to home page'):
        home_screen = HomeScreen(get_driver)
    with allure.step('Open Dnepr catalog screen'):
        home_screen.click_catalog_on_home_page()
        catalog_screen = CatalogScreen(get_driver)
        catalog_screen.click_dnepr_parts_catalog()
        catalog_screen.check_catalog_label_element('Запчасти Днепр МТ')
    with allure.step('Group list by text'):
        catalog_screen.select_groups_by_text()
    with allure.step('Assert icon sorting view panels'):
        catalog_screen.check_list_sorting()
    with allure.step('Sorting by rating'):
        catalog_screen.click_list_sorting()
        catalog_screen.select_sorting_by_rating()
    with allure.step('Assert sorting by'):
        catalog_screen.check_sorting_by('По рейтингу')
    with allure.step('Assert basket button for item in list'):
        catalog_screen.check_item_basked_button()
