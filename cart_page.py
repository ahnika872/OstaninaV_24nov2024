import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.step("Страница корзины")
class CartPage:
    def __init__(self, driver):
        """
        Инициализация класса CartPage.

        :param driver: WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    @allure.step("Открытие сайта")
    def open_site(self):
        """
        Открывает сайт по умолчанию.
        """
        self.driver.get("https://www.sibdar-spb.ru/")

    @allure.step("Навигация к продуктам")
    def navigate_to_products(self):
        """
        Переходит к разделу 'Продукция'.
        """
        products_button = self.driver.find_element(By.LINK_TEXT, "Продукция")
        products_button.click()

    @allure.step("Добавление продукта в корзину")
    def add_product_to_cart(self):
        """
        Добавляет продукт в корзину.
        """
        product_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bx_3218110189_204"]'))
        )
        add_to_cart_button = product_element.find_element(By.XPATH, 
            './/button[@class="btn-default js-order" and @onclick="addToCard(\'204\', this, event);"]'
        )
        add_to_cart_button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переходит в корзину для просмотра добавленных товаров.
        """
        basket_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/a'))
        )
        basket_link.click()

    @allure.step("Проверка наличия продукта в корзине")
    def is_product_in_cart(self):
        """
        Проверяет, добавлен ли продукт в корзину.

        :return: True, если продукт отображается в корзине, иначе False.
        """
        added_product = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name_product_item_204"]'))
        )
        return added_product.is_displayed()

    @allure.step("Получение количества продукта в корзине")
    def get_product_quantity(self):
        """
        Получает количество данного продукта в корзине.

        :return: Количество продукта.
        """
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'count_product_item_204'))
        )
        return quantity_input.get_attribute('value')
