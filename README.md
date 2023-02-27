# автотесты для сервиса Stellar Burgers -- https://stellarburgers.nomoreparties.site

test_register
    
    Регистрация 
        -- успешная регистрация
        поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен:
        например, 123@ya.ru. Минимальный пароль — шесть символов
        -- ошибка для некорректного пароля

test_login

    Вход
        -- по кнопке «Войти в аккаунт» на главной,
        -- через кнопку «Личный кабинет»,
        -- через кнопку в форме регистрации,
        -- через кнопку в форме восстановления пароля

test_profile

    Переход в личный кабинет
        -- по клику на «Личный кабинет»

test_from_profile_to_burgerconstructor

    Переход из личного кабинета в конструктор
        -- по клику на «Конструктор»
        -- по клику на логотип Stellar Burgers

test_logout

    Выход из аккаунта
        -- по кнопке «Выйти» в личном кабинете

test_burgerconstructor

    Раздел «Конструктор» 
        -- переход к разделу «Булки»
        -- переход к разделу «Соусы»
        -- переход к разделу «Начинки»