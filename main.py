import flet as ft

import Registr
from Money import MoneyContainer


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = True

    registr_page = Registr.Registration(page)

    login = ft.TextField(label='Логин', color=ft.colors.WHITE, width=400, height=70,
                         border_color=ft.colors.AMBER, border_radius=5)

    password = ft.TextField(label="Пароль",
                            color=ft.colors.WHITE, width=400,
                            password=True, can_reveal_password=True,
                            height=70,
                            border_color=ft.colors.AMBER, border_radius=5)

    b = ft.ElevatedButton(text="Войти", on_click=registr_page.login_account)

    registr = ft.TextButton(text="Создать аккаунт",
                            width=180,
                            height=30,
                            on_click=lambda _: page.go("/registration"))

    page_login = ft.Container(
        content=ft.Column(wrap=True, controls=[login, password, ft.Row([b, registr])])
    )

    # def registration(e):
    #    page.route = "/registration"
    #    page.controls.clear()
    #    page.controls.append()
    #    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/", controls=[page_login], vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        if page.route == "/registration":
            page.views.append(
                ft.View(
                    "/registration",
                    controls=[registr_page],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        elif page.route == "/golden_coin":
            page.views.append(
                ft.View(
                    "/golden_coin",
                    controls=[MoneyContainer(page)],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    t = ft.Text()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
