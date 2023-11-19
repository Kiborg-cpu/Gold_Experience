import flet as ft


class MoneyContainer(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.money_text = ft.TextField(label='Введите количество денег', color=ft.colors.WHITE, width=400, height=70,
                                       border_color=ft.colors.AMBER, border_radius=5)
        self.buy_add = ft.TextButton(text='+', width=180, height=30)
        self.content = ft.Column(wrap=True,
                                 controls=[self.money_text, self.buy_add])
