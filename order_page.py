import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.step("Страница оформления заказа")
class OrderPage:
    def __init__(self, driver):
        """
        Инициализация класса OrderPage.

        :param driver: WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    @allure.step("Открытие сайта по URL")
    def open_site(self, url):
        """
        Открывает указанный URL в браузере.

        :param url: URL сайта, который нужно открыть.
        """
        self.driver.get(url)

    @allure.step("Клик на кнопку 'Продукция'")
    def click_products_button(self):
        """
        Нажимает на кнопку 'Продукция' для перехода к списку товаров.
        """
        products_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Продукция"))
        )
        products_button.click()

    @allure.step("Клик на кнопку 'Узнать оптовую цену'")
    def click_wholesale_price_button(self):
        """
        Нажимает на кнопку 'Узнать оптовую цену' для открытия формы заказа.
        """
        wholesale_price_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@class="opt order" and @onclick="modal_order(event);"]')
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", wholesale_price_button)
        wholesale_price_button.click()

    @allure.step("Заполнение поля 'Имя'")
    def fill_name(self, name):
        """
        Заполняет поле 'Имя' в форме заказа.

        :param name: Имя пользователя для заполнения.
        """
        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="req" and @name="Имя"]'))
        )
        name_input.click()
        name_input.send_keys(name)

    @allure.step("Заполнение поля 'Телефон'")
    def fill_phone(self, phone):
        """
        Заполняет поле 'Телефон' в форме заказа.

        :param phone: Номер телефона для заполнения.
        """
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="ph req" and @name="Телефон"]'))
        )
        phone_input.click()
        phone_input.send_keys(phone)

    @allure.step("Клик на кнопку 'Отправить'")
    def click_send_button(self):
        """
        Нажимает на кнопку 'Отправить' для отправки формы заказа.
        """
        send_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="flex btn-default btnsendajax"]'))
        )
        send_button.click()

    @allure.step("Получение сообщения об успешной отправке")
    def get_success_message(self):
        """
        Проверяет наличие сообщения об успешной отправке заявки.

        :return: True, если сообщение отображается, иначе False.
        """
        success_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//h3[text()="Спасибо, Ваша заявка отправлена!"]'))
        )
        return success_message.is_displayed()
