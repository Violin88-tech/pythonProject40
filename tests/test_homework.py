import allure

from demoqa_tests.pages.registration_pages import RegistrationPage
from demoqa_tests.data.users import test_user


def test_registration():
    registration_page = RegistrationPage()
    with allure.step("Открываем форму регистрации"):
        registration_page.open_registration_page()
    with allure.step("Регистрируем пользователя"):
        registration_page.register(test_user)
    with allure.step("Проверяем успешность регистрации (введённые данные с отображаемыми)"):
        registration_page.should_registered_user_with(test_user)
