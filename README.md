# Sprint_5
Проект автоматизации тестирования веб-приложения Stellar Burgers:

Основной фреймворк для написания автотестов — pytest.
Основные технологии:

Язык программирования: Python.
Фреймворк для тестирования: pytest.
Инструмент для автоматизации тестов: Selenium WebDriver.
Установка проекта:

Клонируйте репозиторий проекта:
bash
Copy code
git clone https://github.com/LOS32/Sprint_5.git
Перейдите в директорию проекта:
bash
Copy code
cd <Sprint_5>

Запуск тестов:

Для запуска всех тестов выполните:
bash
Copy code
pytest -v
Для запуска отдельного файла с тестами используйте:
bash
Copy code
pytest <путь-к-файлу-с-тестами> -v
Структура проекта:

conftest.py: содержит общие фикстуры для тестов.
locators.py: содержит локаторы элементов для тестов.
helpers.py: содержит функцию для генерации рандомных email и password
data.py: содержит данные user_name, user_email, user_password и URL
test_login_by_login_account_button.py: тесты для проверки входа в аккаунт через кнопки Войти в разных окнах.
test_from_personal_account_to_constructor_and_logo.py: тесты для проверки переходов из личного кабинета в конструктор и по логотипу.
test_logout.py: тесты для проверки выхода из аккаунта.
test_registration_form.py: тесты для проверки формы регистрации.
test_section_constructor.py: тесты для проверки переходов между разделами конструктора (Булки, Соусы, Начинки).
