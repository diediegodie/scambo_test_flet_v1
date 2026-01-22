"""Configurations page with theme switching and settings.

Allows users to toggle between dark and light modes and access other app settings.
Future-ready for additional configuration options.
"""

import flet as ft
from ..widgets.nav_bar import create_nav_bar
from ..theme import AppTheme, get_light_theme, get_dark_theme


def configurations(page: ft.Page, is_dark_mode: bool = False):
    """
    Settings and configurations page with theme toggle.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Current theme state (dark mode on/off)
    """
    page.title = "Configurações - Scambo"
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    def toggle_theme(e):
        """Toggle between dark and light themes and refresh the page."""
        # Toggle the theme state
        new_dark_mode = not is_dark_mode
        
        # Update page theme
        page.theme = get_dark_theme() if new_dark_mode else get_light_theme()
        page.bgcolor = (
            AppTheme.DARK_BACKGROUND if new_dark_mode else AppTheme.LIGHT_BACKGROUND
        )
        page.update()
        
        # Reload the configurations page with new theme
        page.clean()
        configurations(page, new_dark_mode)

    # Page title
    title = ft.Text(
        "Configurações",
        size=AppTheme.FONT_SIZE_TITLE,
        weight=AppTheme.FONT_WEIGHT_BOLD,
        color=(
            AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY
        ),
    )

    # Theme section header
    theme_section_title = ft.Text(
        "Aparência",
        size=AppTheme.FONT_SIZE_SUBTITLE,
        weight=AppTheme.FONT_WEIGHT_MEDIUM,
        color=(
            AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY
        ),
    )

    # Theme description
    theme_description = ft.Text(
        "Escolha o tema do aplicativo",
        size=AppTheme.FONT_SIZE_BODY,
        color=(
            AppTheme.DARK_TEXT_SECONDARY
            if is_dark_mode
            else AppTheme.LIGHT_TEXT_SECONDARY
        ),
    )

    # Current theme indicator
    current_theme_text = ft.Text(
        f"Tema atual: {'Escuro' if is_dark_mode else 'Claro'}",
        size=AppTheme.FONT_SIZE_BODY,
        weight=AppTheme.FONT_WEIGHT_MEDIUM,
        color=(
            AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY
        ),
    )

    # Theme toggle button with icon
    theme_toggle_button = ft.Container(
        content=ft.Row(
            [
                ft.Icon(
                    ft.Icons.DARK_MODE if is_dark_mode else ft.Icons.LIGHT_MODE,
                    color=AppTheme.PRIMARY_GREEN,
                    size=AppTheme.ICON_SIZE_LG,
                ),
                ft.Text(
                    "Alternar para modo claro" if is_dark_mode else "Alternar para modo escuro",
                    size=AppTheme.FONT_SIZE_BODY,
                    weight=AppTheme.FONT_WEIGHT_MEDIUM,
                    color=(
                        AppTheme.DARK_TEXT_PRIMARY
                        if is_dark_mode
                        else AppTheme.LIGHT_TEXT_PRIMARY
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=AppTheme.SPACING_SM,
        ),
        bgcolor=AppTheme.PRIMARY_GREEN,
        border_radius=AppTheme.CARD_BORDER_RADIUS,
        padding=ft.padding.symmetric(
            horizontal=AppTheme.SPACING_LG, vertical=AppTheme.SPACING_MD
        ),
        on_click=toggle_theme,
        # Add hover effect for better UX
        ink=True,
    )

    # Settings card container
    settings_card = AppTheme.get_card_container(
        content=ft.Column(
            [
                theme_section_title,
                ft.Container(height=AppTheme.SPACING_XS),
                theme_description,
                ft.Container(height=AppTheme.SPACING_SM),
                current_theme_text,
                ft.Container(height=AppTheme.SPACING_MD),
                theme_toggle_button,
                ft.Container(height=AppTheme.SPACING_LG),
                AppTheme.get_divider(is_dark_mode),
                ft.Container(height=AppTheme.SPACING_LG),
                # Placeholder for future settings sections
                ft.Text(
                    "Mais opções em breve...",
                    size=AppTheme.FONT_SIZE_CAPTION,
                    color=(
                        AppTheme.DARK_TEXT_TERTIARY
                        if is_dark_mode
                        else AppTheme.LIGHT_TEXT_TERTIARY
                    ),
                    italic=True,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=0,
        ),
        is_dark_mode=is_dark_mode,
        width=AppTheme.CARD_WIDTH_STANDARD,
    )

    # Main content with scrolling
    content = ft.Column(
        [
            ft.Container(height=AppTheme.SPACING_LG),
            title,
            ft.Container(height=AppTheme.SPACING_MD),
            settings_card,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    # Bottom navigation bar
    nav_bar = create_nav_bar(page, selected_index=5, is_dark_mode=is_dark_mode)

    # Build page layout
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=content,
                    expand=True,
                ),
                nav_bar,
            ],
            spacing=0,
            expand=True,
        )
    )
