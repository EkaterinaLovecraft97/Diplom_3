from selenium.webdriver.common.by import By

class AccountPageLocators:
    # Раздел "Профиль"
    profile = (By.XPATH, '//a[@href = "/account/profile"]')

    # Раздел "История заказов"
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Кнопка "Выйти"
    button_logout = (By.XPATH, '//button[@type = "button"]')

    # Кнопка "Зарегистрироваться"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Описание раздела: "В этом разделе вы можете изменить свои персональные данные"
    description_of_section = (By.XPATH, '//p[contains(@class, "Account_text")]')


class FeedPageLocators:
    # Раздел заказов
    section_orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    title_of_orders_feed = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Карточка заказа в ленте
    order_in_feed = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Всплывающее окно с деталями заказа
    modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')

    # Заголовок всплывающего окна с деталями заказа
    title_of_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    # Счетчик заказов "Выполнено за все время"
    quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик заказов "Выполнено за сегодня"
    daily_quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Заказ в разделе "В работе"
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Номер заказа в разделе "В работе"
    number_of_order_in_progress = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')

    # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
    id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной
    button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')

    # Кнопка "Оформить заказ"
    button_make_the_order = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Кнопка "Конструктор" в шапке сайта
    header_of_page_constructor = (By.XPATH, '//p[text() = "Конструктор"]')

    # Селектор, помечающий выбранный раздел конструктора как активный
    selected_button = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'))

    # Заголовок раздела "Конструктор"
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Заголовок раздела "Булки" в меню конструктора
    buns_block = (By.XPATH, '//span[text() = "Булки"]')

    # Заголовок раздела "Соусы" в меню конструктора
    sauces_block = (By.XPATH, '//span[text() = "Соусы"]')

    # Заголовок раздела "Начинки" в меню конструктора
    fillings_block = (By.XPATH, '//span[text() = "Начинки"]')

    # Кнопка "Лента заказов"
    button_order_feed_in_header = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    # Ингредиент
    ingredient_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

    # Заголовок окна "Детали ингредиента"
    header_of_modal_details = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    button_close_modal = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')

    # Картинка ингредиента в общем списке
    burger_ingredient = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Куда перетаскиваются игнредиенты
    place_for_ingredients = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Состав заказа в условной "Корзине"
    content_of_order = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')

    # Кнопка "Оформить заказ"
    button_make_order = (By.CLASS_NAME, 'button_button__33qZ0')

    # Количество экземпляров ингредиента в заказе (счетчик)
    count_of_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')

    # Окно подтверждения создания заказа
    confirmation_modal_of_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')

    # Номер созданного заказа в окне подтверждения
    number_of_order_in_modal_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    button_close_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'
                                           ']//button[contains(@class, "close")]')

class OrderHistoryPageLocators:
    # Карточка заказа в истории заказов
    order_card = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    # Заголовок карточки заказа с названием бургера
    order_card_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    # Номер заказа в карточке заказа
    order_card_id = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')


class PasswordRecoveryLocators:
    # Кнопка "Восстановить пароль" на экране входа
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Поле ввода email
    input_email = (By.CLASS_NAME, 'input__textfield')

    # Кнопка "Восстановить" на странице ввода email
    button_recover = (By.CLASS_NAME, 'button_button__33qZ0')

    # Поле ввода пароля
    input_password = (By.CSS_SELECTOR, '.input_type_password .input__textfield')

    # Иконка, скрывающая (боль) пароль
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Пароль со статусом видимости
    value_password_is_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')
    # Пароль скрыт
    value_password_is_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                             '"input_type_password")]')
