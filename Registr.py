import flet as ft
import sqlite3


class Registration(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.login = ft.TextField(label='Придумайте никнейм', color=ft.colors.WHITE, width=400, height=70,
                                  border_color=ft.colors.AMBER, border_radius=5)
        self.nPassword = ft.TextField(label='Придумайте пароль', color=ft.colors.WHITE, width=400, height=70,
                                      border_color=ft.colors.AMBER, border_radius=5)
        self.create = ft.TextButton(text='Создать аккаунт', width=180,
                                    height=30, on_click=self.create_account)
        self.cancel = ft.TextButton(text='Вернуться на главную', width=180,
                                    height=30, on_click=lambda _: self.page.go("/"))
        self.info = ft.Text(weight=ft.FontWeight.BOLD)
        self.content = ft.Column(wrap=True,
                                 controls=[self.login, self.nPassword, ft.Row([self.create, self.cancel]), self.info])

    def create_account(self, arg):
        database = sqlite3.connect("log_people")
        cursor = database.cursor()

        # Создаем таблицу 'users', если ее нет
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            login TEXT,
            password TEXT,
            money INTEGER
        )""")
        database.commit()

        # Проверяем, существует ли уже логин
        cursor.execute("SELECT login FROM users WHERE login = ?", (self.login.value,))
        existing_login = cursor.fetchone()

        if existing_login is None:
            # Если логин не существует, вставляем нового пользователя
            cursor.execute("INSERT INTO users VALUES (?, ?, 0)", (self.login.value, self.nPassword.value))
            database.commit()
            self.page.go("/golden_coin")
        else:
            self.login.border_color = ft.colors.RED
            self.nPassword.border_color = ft.colors.RED
            self.info.color = ft.colors.RED
            self.info.value = f'ТАКОЙ НИКНЕЙМ УЖЕ ЕСТЬ: {self.login.value}'
            self.update()
            print(f'Такой логин уже есть: {self.login.value}')

        # Закрываем соединение с базой данных
        database.close()

    def login_account(self, arg):
        database = sqlite3.connect("log_people")
        cursor = database.cursor()

        # Проверяем, существует ли уже логин
        cursor.execute("SELECT login, money FROM users WHERE login = ?", (self.login.value,))
        existing_login = cursor.fetchone()

        if existing_login is not None:
            self.page.go("/golden_coin")

        database.close()
