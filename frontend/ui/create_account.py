import flet as ft


def create_account(page: ft.Page):
    """User registration page with consistent styling to the login page."""
    page.title = "Criar conta"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"

    # Logo or title (consistent with login page)
    logo = ft.Text(
        "Rede de Trocas", size=30, weight=ft.FontWeight.BOLD, color="#333"
    )

    # Registration fields
    full_name = ft.TextField(
        label="Nome completo",
        hint_text="Digite seu nome completo",
        width=300,
        prefix_icon=ft.Icons.PERSON,
        border_radius=10,
    )
    email = ft.TextField(
        label="Email",
        hint_text="Digite seu email",
        width=300,
        prefix_icon=ft.Icons.EMAIL,
        border_radius=10,
    )
    phone = ft.TextField(
        label="Telefone",
        hint_text="Digite seu telefone",
        width=300,
        prefix_icon=ft.Icons.PHONE,
        border_radius=10,
    )
    password = ft.TextField(
        label="Senha",
        hint_text="Crie uma senha",
        password=True,
        can_reveal_password=True,
        width=300,
        prefix_icon=ft.Icons.LOCK,
        border_radius=10,
    )
    confirm_password = ft.TextField(
        label="Confirmar senha",
        hint_text="Repita a senha",
        password=True,
        can_reveal_password=True,
        width=300,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        border_radius=10,
    )

    # Placeholder registration handler
    status_text = ft.Text("")

    def handle_create_account(e):
        # Placeholder action: update status text; integration will be added later.
        status_text.value = "Cadastro enviado (placeholder)"
        status_text.color = "green"
        page.update()

    create_btn = ft.ElevatedButton(
        text="Criar conta",
        width=300,
        bgcolor="#4CAF50",
        color="white",
        on_click=handle_create_account,
    )

    # Optional: back to login link
    def go_to_login(e):
        from frontend.ui.login_page import main as login_page_main
        page.clean()
        login_page_main(page)

    back_to_login = ft.TextButton(
        "Já tem uma conta? Entrar",
        on_click=go_to_login,
    )

    # Central card
    form = ft.Column(
        [
            logo,
            full_name,
            email,
            phone,
            password,
            confirm_password,
            create_btn,
            status_text,
            back_to_login,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    register_card = ft.Card(
        content=ft.Container(
            content=form,
            padding=30,
            width=400,
        )
    )

    page.add(register_card)


if __name__ == "__main__":
    ft.app(target=create_account)
