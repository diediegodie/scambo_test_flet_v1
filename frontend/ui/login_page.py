import flet as ft
from frontend.ui.dashboard_page import dashboard
from frontend.ui.create_account import create_account


def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"

    # Logo or title
    logo = ft.Text("Rede de Trocas", size=30, weight=ft.FontWeight.BOLD, color="#333")

    # Login fields
    email = ft.TextField(
        label="Email",
        hint_text="Digite seu email",
        width=300,
        prefix_icon=ft.Icons.EMAIL,
        border_radius=10,
    )
    password = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        can_reveal_password=True,
        width=300,
        prefix_icon=ft.Icons.LOCK,
        border_radius=10,
    )

    # Login button
    def login_click(e):
        # Here you can validate and redirect to the dashboard
        page.clean()
        dashboard(page)

    login_btn = ft.ElevatedButton(
        text="Entrar",
        width=300,
        bgcolor="#4CAF50",
        color="white",
        on_click=login_click,
    )

    # Create account link
    def go_to_create_account(e):
        page.clean()
        create_account(page)

    create_account_link = ft.TextButton(
        "Criar uma conta",
        on_click=go_to_create_account,
    )

    # Central card
    login_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [logo, email, password, login_btn, create_account_link],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=30,
            width=400,
        )
    )

    page.add(login_card)


if __name__ == "__main__":
    ft.app(target=main)
