from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    #кнопка войти в аккаунт на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    #поле имя в форме входа в аккаунт
    LOGIN_NAME_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # поле пароль в форме входа в аккаунт
    PASSWORD_NAME_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    #кнопка личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    #ссылка на кнопку формы регистрации
    LINK_TO_REGISTRATION_FORM = (By.XPATH, "//a[@href='/register' and text()='Зарегистрироваться']")
    #кнопка войти на основной форме входа
    LOGIN_BUTTON_MAIN_FORM = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']")
    # кнопка войти на форме регистрации
    LOGIN_BUTTON_REGISTRATION_FORM = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    # кнопка восстановить пароль
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    #кнопка войти в форме восстановления пароля
    LOGIN_BUTTON_RECOVERY_FORM = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    #поле имя в форме регистрации
    REGISTRATION_NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # поле Email в форме регистрации
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    #поле пароль в форме регистрации
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # кнопка зарегистрироваться в форме регистрации
    BUTTON_SUBMIT_REGISTRATION = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and text()='Зарегистрироваться']")
    # логотип Stellar Burgers для перехода на главную страницу
    LOGO_BUTTON = (By.XPATH, "//a[@href='/']")
    # кнопка выйти в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # кнопка конструктор
    CONSTRUCTOR_BUTTON = (By.CLASS_NAME, "AppHeader_header__linkText__3q_va")
    #сообщение об ошибке в поле пароль
    ERROR_MSSAGE = (By.CLASS_NAME, "input__error")
    # разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    #проверка активна ли вкладка Соусы
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
    # проверка активна ли вкладка Начинки
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
    # проверка активна ли вкладка Булки
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
    # класс активной кнопки с секцией ингридиента в конструкторе
    TAB_ACTIVE_CLASS = "tab_tab_type_current__2BEPc"



