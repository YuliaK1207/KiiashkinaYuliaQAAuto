import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваємо сторінку https://github.com/login
    driver.get('https://github.com/login')

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, 'login_field')

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys('sergiibutenko@mistakeinemail.com')
    
    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, 'password')

    # Вводимо неправильний пароль
    pass_elem.send_keys('wrong password')
    
    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, 'commit')

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == 'Sign in to GitHub · GitHub'

    # Закриваємо браузер
    driver.close()


# Individual Task

# Тест, що перевіряє пошук посилки на сайті "Нова Пошта"
@pytest.mark.ui
def test_check_incorrect_parcel_tracking_number():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваємо сторінку https://tracking.novaposhta.ua
    driver.get('https://tracking.novaposhta.ua')

    # Знаходимо поле, в яке будемо вводити неправильний трекінговий номер посилки 
    tracking_number_elem = driver.find_element(By.ID, 'en')

    # Вводимо неправильний трекінговий номер посилки
    tracking_number_elem.send_keys('12345000000000')

    # Емулюємо натискання кнопки search
    tracking_number_elem.send_keys(Keys.ENTER)

    # Закриваємо браузер
    driver.close()