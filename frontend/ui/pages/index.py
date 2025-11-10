import flet as ft
from .login import main as login_page
from .create_account import create_account


def index(page: ft.Page):
    """Landing page with navigation to login and create account."""
    page.title = "SCAMBO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"

    # Navigation handlers
    def go_to_login(_):
        page.clean()
        login_page(page)

    def go_to_create_account(_):
        page.clean()
        create_account(page)

    # Logo
    logo = ft.Text(
        "SCAMBO",
        size=100,
        weight=ft.FontWeight.BOLD,
        color="#4CAF50",
        text_align=ft.TextAlign.CENTER,
    )

    # Buttons
    buttons = ft.Row(
        [
            ft.ElevatedButton(
                text="Entrar",
                width=150,
                height=50,
                bgcolor="#4CAF50",
                color="white",
                on_click=go_to_login,
            ),
            ft.OutlinedButton(
                text="Criar Conta",
                width=150,
                height=50,
                on_click=go_to_create_account,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    # Main content
    page.add(
        ft.Column(
            [
                logo,
                ft.Container(height=30),
                buttons,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=index)
