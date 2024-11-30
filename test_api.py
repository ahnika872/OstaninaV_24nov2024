import requests
import pytest
import allure

BASE_URL = "https://www.sibdar-spb.ru/ajax/basketOrder.php"

TEST_DATA_ADD = {
    "idCookie": "780423",
    "idProd": "373",
    "type": "add",
}
 
COOKIE_VALUE = "Shk5bHJSluS8ecJHUOB5TN1aEgQeISKm" 

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
@pytest.mark.parametrize("test_data", [TEST_DATA_ADD])
def test_add_to_cart(test_data):
    """Тест на добавление товара в корзину."""
    
    headers = {'Cookie': f'PHPSESSID={COOKIE_VALUE}'}
    response = requests.post(BASE_URL, json=test_data, headers=headers)

    assert response.status_code == 200, "Неожиданный код статуса."


@pytest.fixture
def cookies():
    return {
        'PHPSESSID': COOKIE_VALUE
    }

@allure.feature("Корзина")
@allure.story("Изменение количества товара")
def test_change_quantity(cookies):
    """Тест на изменение количества товара в корзине."""
    
    data = {"idCookie": "780423", "idProd": 259, "type": "plus"}
    response = requests.post(BASE_URL, json=data, cookies=cookies)
    
    assert response.status_code == 200, "Не удалось изменить количество товара."


@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
@pytest.mark.parametrize("item_id", [1, 2, 3])
def test_delete_from_cart(item_id):
    """Тест на удаление товара из корзины."""
    
    data = {"idCookie": "780423", "idProd": item_id, "type": "remove"}
    response = requests.post(BASE_URL, json=data, cookies={'PHPSESSID': COOKIE_VALUE})
    
    assert response.status_code == 200, f"Не удалось удалить товар с id {item_id}."

