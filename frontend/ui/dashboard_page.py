import flet as ft

def dashboard(page: ft.Page):
    page.title = "Dashboard - Rede de Trocas"
    page.bgcolor = "#f9f9f9"

    # App bar
    appbar = ft.AppBar(
        title=ft.Text("Rede de Trocas"),
        bgcolor="#4CAF50",
        color="white",
        actions=[
            ft.IconButton(icon=ft.Icons.SEARCH),
            ft.IconButton(icon=ft.Icons.NOTIFICATIONS),
            ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE),
        ],
    )

    # Welcome message
    welcome = ft.Text(
        "Bem-vindo, Diego 👋",
        size=22,
        weight=ft.FontWeight.BOLD,
        color="#333",
    )

    # Items/services feed
    feed = ft.ListView(
        expand=True,
        spacing=10,
        controls=[
            ft.Card(
                content=ft.ListTile(
                    leading=ft.CircleAvatar(bgcolor="blue", content=ft.Text("B")),
                    title=ft.Text("Bicicleta usada"),
                    subtitle=ft.Text("Troco por notebook ou celular"),
                    trailing=ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
                )
            ),
            ft.Card(
                content=ft.ListTile(
                    leading=ft.CircleAvatar(bgcolor="green", content=ft.Text("A")),
                    title=ft.Text("Aula de violão 🎸"),
                    subtitle=ft.Text("Disponível aos finais de semana"),
                    trailing=ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
                )
            ),
            ft.Card(
                content=ft.ListTile(
                    leading=ft.CircleAvatar(bgcolor="red", content=ft.Text("N")),
                    title=ft.Text("Notebook antigo"),
                    subtitle=ft.Text("Troco por bicicleta ou serviços"),
                    trailing=ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
                )
            ),
        ],
    )

    # inferior navigation bar
    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Novo"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ]
    )

    # principal layout
    page.add(
        appbar,
        ft.Column(
            [welcome, feed],
            expand=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        ),
        nav,
    )
