import flet as ft
from .dashboard import dashboard
from .create_account import create_account
from ..theme import AppTheme


def main(page: ft.Page, is_dark_mode: bool = False):
    """
    Login page with email and password fields.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )

    # Logo or title
    logo = ft.Text(
        "Login",
        size=AppTheme.FONT_SIZE_TITLE + 6,
        weight=AppTheme.FONT_WEIGHT_BOLD,
        color=(
            AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY
        ),
    )

    # Login fields
    email = AppTheme.get_input_field(
        label="Email",
        hint_text="Digite seu email",
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.EMAIL,
    )
    password = AppTheme.get_input_field(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
        prefix_icon=ft.Icons.LOCK,
        can_reveal_password=True,
    )

    # Login button
    def login_click(e):
        # Here you can validate and redirect to the dashboard
        page.clean()
        dashboard(page, is_dark_mode)

    login_btn = AppTheme.get_elevated_button(
        text="Entrar",
        on_click=login_click,
        is_dark_mode=is_dark_mode,
        width=AppTheme.INPUT_FIELD_WIDTH,
    )

    # Create account link
    def go_to_create_account(e):
        page.clean()
        create_account(page, is_dark_mode)

    create_account_link = AppTheme.get_text_button(
        text="Criar uma conta",
        on_click=go_to_create_account,
        is_dark_mode=is_dark_mode,
    )

    # Central card
    login_card = ft.Card(
        elevation=AppTheme.CARD_ELEVATION,
        color=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
        content=ft.Container(
            content=ft.Column(
                [logo, email, password, login_btn, create_account_link],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=AppTheme.SPACING_LG,
            ),
            padding=AppTheme.SPACING_XL,
            width=AppTheme.CARD_WIDTH_NARROW,
            border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
        ),
    )

    page.add(login_card)


if __name__ == "__main__":
    ft.app(target=main)
