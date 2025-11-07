import flet as ft

def main(page: ft.Page):
    page.title = "Login - Rede de Trocas"
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

    # Central card
    login_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [logo, email, password, login_btn],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=30,
            width=400,
        )
    )

    page.add(login_card)


def dashboard(page: ft.Page):
    page.title = "Dashboard - Rede de Trocas"
    page.bgcolor = "white"

    # App bar
    appbar = ft.AppBar(
        title=ft.Text("Dashboard"),
        bgcolor="#4CAF50",
        color="white",
    )

    # Dashboard content
    welcome = ft.Text("Bem-vindo à Rede de Trocas!", size=24, weight=ft.FontWeight.BOLD)
    feed = ft.ListView(
        controls=[
            ft.ListTile(title=ft.Text("Item 1 - Bicicleta usada")),
            ft.ListTile(title=ft.Text("Serviço - Aula de violão")),
            ft.ListTile(title=ft.Text("Item 2 - Notebook antigo")),
        ],
        expand=True,
    )

    page.add(appbar, ft.Column([welcome, feed], spacing=20, expand=True))


ft.app(target=main)
