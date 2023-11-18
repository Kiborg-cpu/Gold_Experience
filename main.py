import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = True

    def button_clicked(e):
        t.value = f"Textboxes values are:  '{login.value}', '{password.value}'."
        page.update()

        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def registration(e):
        page.route = "/registration"
        page.controls.clear()
        page.update()

    t = ft.Text()

    default = ft.TextField(label='Default', color=ft.colors.WHITE, width=400, height=70,
                         border_color=ft.colors.AMBER, border_radius=5)

    login = ft.TextField(label='Логин', color=ft.colors.WHITE, width=400, height=70,
                         border_color=ft.colors.AMBER, border_radius=5)

    password = ft.TextField(label="Пароль",
                            color=ft.colors.WHITE, width=400,
                            password=True, can_reveal_password=True,
                            height=70,
                            border_color=ft.colors.AMBER, border_radius=5)

    b = ft.ElevatedButton(text="Войти", on_click=button_clicked)

    registr = ft.TextButton(text="Создать аккаунт",
                            width=180,
                            height=30,
                            on_click=registration)

    page_login = ft.Container(
        content=ft.Column(wrap=True, controls=[login, password, ft.Row([b, registr])])
    )

    page.add(page_login)


ft.app(target=main)  # view=ft.WEB_BROWSER
