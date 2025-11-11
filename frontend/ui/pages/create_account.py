import flet as ft
from ..theme import AppTheme


def create_account(page: ft.Page, is_dark_mode: bool = False):
    """
    User registration page with consistent styling to the login page.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """
    page.title = "Criar conta"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )

    # Logo or title (consistent with login page)
    logo = ft.Text(
        "Rede de Trocas",
        size=AppTheme.FONT_SIZE_TITLE + 6,
        weight=AppTheme.FONT_WEIGHT_BOLD,
        color=(
            AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY
        ),
    )

    # Registration fields
    full_name = AppTheme.get_input_field(
        label="Nome completo",
        hint_text="Digite seu nome completo",
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.PERSON,
    )
    email = AppTheme.get_input_field(
        label="Email",
        hint_text="Digite seu email",
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.EMAIL,
    )
    phone = AppTheme.get_input_field(
        label="Telefone",
        hint_text="Digite seu telefone",
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.PHONE,
    )
    password = AppTheme.get_input_field(
        label="Senha",
        hint_text="Crie uma senha",
        password=True,
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.LOCK,
        can_reveal_password=True,
    )
    confirm_password = AppTheme.get_input_field(
        label="Confirmar senha",
        hint_text="Repita a senha",
        password=True,
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        can_reveal_password=True,
    )

    # Placeholder registration handler
    status_text = ft.Text("", color=AppTheme.SUCCESS)

    def handle_create_account(e):
        # Placeholder action: update status text; integration will be added later.
        status_text.value = "Cadastro enviado (placeholder)"
        page.update()

    create_btn = AppTheme.get_elevated_button(
        text="Criar conta",
        on_click=handle_create_account,
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
    )

    # Optional: back to login link
    def go_to_login(e):
        from frontend.ui.pages.login import main as login_page_main

        page.clean()
        login_page_main(page, is_dark_mode)

    back_to_login = AppTheme.get_text_button(
        text="Já tem uma conta? Entrar",
        on_click=go_to_login,
        is_dark_mode=is_dark_mode,
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
        spacing=AppTheme.SPACING_LG,
    )

    register_card = ft.Card(
        elevation=AppTheme.CARD_ELEVATION,
        color=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
        content=ft.Container(
            content=form,
            padding=AppTheme.SPACING_XL,
            width=AppTheme.CARD_WIDTH_NARROW,
            border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
        ),
    )

    page.add(register_card)


if __name__ == "__main__":
    ft.app(target=create_account)
