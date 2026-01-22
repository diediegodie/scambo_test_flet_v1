import flet as ft
from .login import main as login_page
from .create_account import create_account
from ..theme import AppTheme


# Landing page with navigation to login and create account.
def index(page: ft.Page, is_dark_mode: bool = False):
    """
    Landing page with logo and navigation buttons.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """
    page.title = "SCAMBO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )

    # Navigation handlers
    def go_to_login(_):
        page.clean()
        login_page(page, is_dark_mode)

    def go_to_create_account(_):
        page.clean()
        create_account(page, is_dark_mode)

    # Logo
    logo = ft.Text(
        "SCAMBO",
        size=AppTheme.LOGO_SIZE,
        weight=AppTheme.FONT_WEIGHT_BOLD,
        color=AppTheme.PRIMARY_GREEN,
        text_align=ft.TextAlign.CENTER,
    )

    # Buttons
    buttons = ft.Row(
        [
            AppTheme.get_elevated_button(
                text="Entrar",
                on_click=go_to_login,
                is_dark_mode=is_dark_mode,
                width=AppTheme.LANDING_BUTTON_WIDTH,
                height=AppTheme.BUTTON_HEIGHT,
            ),
            ft.OutlinedButton(
                content="Criar Conta",
                width=AppTheme.LANDING_BUTTON_WIDTH,
                height=AppTheme.BUTTON_HEIGHT,
                on_click=go_to_create_account,
                style=ft.ButtonStyle(
                    side=ft.BorderSide(2, AppTheme.PRIMARY_GREEN),
                    color=AppTheme.PRIMARY_GREEN,
                    shape=ft.RoundedRectangleBorder(radius=AppTheme.CARD_BORDER_RADIUS),
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=AppTheme.SPACING_LG,
    )

    # Main content
    page.add(
        ft.Column(
            [
                logo,
                ft.Container(height=AppTheme.LANDING_SPACER_HEIGHT),
                buttons,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=index)
