import pytest
from selenium import webdriver
from cart_page import CartPage
from order_page import OrderPage
from time import sleep
import allure

@pytest.fixture(scope="module")
def driver():
    """Фикстура для инициализации драйвера Selenium."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
@pytest.mark.critical  # Уровень серьезности
def test_add_to_cart(driver):
    """Тест на добавление товара в корзину."""
    cart_page = CartPage(driver)
    
    # Открываем сайт и добавляем товар в корзину
    cart_page.open_site()
    cart_page.navigate_to_products()
    cart_page.add_product_to_cart()
    cart_page.go_to_cart()
    
    # Проверяем, что товар отображается в корзине
    assert cart_page.is_product_in_cart(), "Товар не найден в корзине"
    allure.step("Тест на добавление товара пройден успешно!")

@allure.feature("Корзина")
@allure.story("Проверка количества товара")
@pytest.mark.high  # Уровень серьезности
def test_check_quantity_in_cart(driver):
    """Тест на проверку количества товара в корзине."""
    cart_page = CartPage(driver)
    cart_page.open_site()
    cart_page.navigate_to_products()
    cart_page.add_product_to_cart()
    
    # Проверяем количество товара в корзине
    cart_page.go_to_cart()  # Переходим в корзину
    quantity_value = cart_page.get_product_quantity()
    
    assert quantity_value == "1 шт", f"Количество товара должно быть '1 шт', но найдено '{quantity_value}'"
    allure.step("Тест на проверку количества товара пройден успешно!")

@allure.feature("Заказ")
@allure.story("Оформление заказа")
@pytest.mark.medium  # Уровень серьезности
def test_order_price(driver):
    """Тест на оформление заказа."""
    order_page = OrderPage(driver)
    
    # Шаг 1: Заходим на сайт
    order_page.open_site("https://www.sibdar-spb.ru/")
    
    # Шаг 2: Нажимаем на кнопку "Продукция"
    order_page.click_products_button()
    sleep(10)  # Подождем, чтобы страница загрузилась

    # Шаг 3: Находим элемент "Узнать оптовую цену" и нажимаем на него
    order_page.click_wholesale_price_button()

    # Шаг 4: Находим поле "Имя" и вводим значение
    order_page.fill_name("Вероника")

    # Шаг 5: Находим поле "Телефон" и вводим значение
    order_page.fill_phone("8888888888")

    # Шаг 6: Находим кнопку "Отправить" и нажимаем на нее
    order_page.click_send_button()
    sleep(10)  # Подождем, чтобы сообщение успело появиться

    # Шаг 7: Проверяем, что появилось сообщение "Спасибо, Ваша заявка отправлена!"
    assert order_page.get_success_message(), "Сообщение об успешной отправке не отображается"
    allure.step("Тест на оформление заказа пройден успешно!")
