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
        self.content = ft.Column(wrap=True, controls=[self.login, self.nPassword, ft.Row([self.create, self.cancel])])

    def create_account(self, arg):
        database = sqlite3.connect("log_people")
        cursor = database.cursor()

        # Создаем таблицу 'users', если ее нет
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            login TEXT,
            password TEXT
        )""")
        database.commit()

        # Проверяем, существует ли уже логин
        cursor.execute("SELECT login FROM users WHERE login = ?", (self.login.value,))
        existing_login = cursor.fetchone()

        if existing_login is None:
            # Если логин не существует, вставляем нового пользователя
            cursor.execute("INSERT INTO users VALUES (?, ?)", (self.login.value, self.nPassword.value))
            database.commit()
        else:
            print(f'Такой логин уже есть: {self.login.value}')

        # Закрываем соединение с базой данных
        database.close()
