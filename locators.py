class Locators:

    authorization_button = "//*[text()='Войти в аккаунт']"  # кнопка Войти в аккаунт
    login_h2 = ".//h2[text()='Вход']"  # заголовок Вход на странице /login
    register_link = ".//a[text()='Зарегистрироваться']"  # ссылка Зарегистрироваться на странице /login
    name_field = 'name'  # поле ввода Имя на странице /register
    email_field = ".//label[text()='Email']//following-sibling::*"  # поле ввода Email на страницах /register и /login
    password_field = ".//input[@name='Пароль']"  # поле ввода Пароль на страницах /register и /login
    register_button = ".//button[text()='Зарегистрироваться']"  # кнопка Зарегистрироваться на странице /register
    incorrect_password_message = ".//p[text()='Некорректный пароль']"  # уведомление Некорректный пароль на странице /register
    login_link = ".//a[text()='Войти']"  # ссылка Войти на странице /register
    login_button = ".//button[text()='Войти']"   # кнопка Войти на странице /login
    forgot_password_link = ".//a[text()='Восстановить пароль']"  # ссылка Восстановить пароль на странице /login
    profile_button = ".//p[text()='Личный Кабинет']"  # кнопка Личный кабинет
    save_button = ".//button[text()='Сохранить']"  # кнопка Сохранить на странице /account/profile
    logout_button = ".//button[text()='Выход']"  # кнопка Выход на странице /account/profile
    constructor_button = ".//p[text()='Конструктор']"  # кнопка Конструктор
    logo = ".//div[@class='AppHeader_header__logo__2D0X2']"  # логотип
    constructor_h1 = ".//h1[text()='Соберите бургер']"   # заголовок Соберите бургер
    buns_section = ".//span[text()='Булки']"  # раздел Булки
    no_select_buns_section = ".//div[contains(@class, 'noselect') and not (contains(@class, 'current'))]/child::span[text()='Булки']" # невыбранный раздел Булки
    select_buns_section = ".//div[contains(@class, 'current')]/child::span[text()='Булки']"  # выбранный раздел Булки
    sauces_section = ".//span[text()='Соусы']"  # раздел Соусы
    select_sauces_section = ".//div[contains(@class, 'current')]/child::span[text()='Соусы']"  # выбранный раздел Соусы
    toppings_section = ".//span[text()='Начинки']"  # раздел Начинки
    select_toppings_section = ".//div[contains(@class, 'current')]/child::span[text()='Начинки']"  # выбранный раздел Начинки
    order_button = ".//button[text()='Оформить заказ']"  # кнопка Оформить заказ