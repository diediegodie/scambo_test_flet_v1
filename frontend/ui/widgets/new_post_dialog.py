"""
Shared component for the "New Post" dialog.
Used by both dashboard and profile pages when clicking "Novo" button.
"""

import flet as ft
from ..theme import AppTheme


def open_new_post_dialog(page: ft.Page, is_dark_mode: bool = False):
    """
    Opens the "New Post" dialog with title, description, and photo placeholder.
    This is a reusable component called from both dashboard and profile pages.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """

    def close_dialog(e):
        dialog.open = False
        page.update()

    def add_photos_placeholder(e):
        # Placeholder for future photo upload functionality
        photo_status.value = "📸 Função de adicionar fotos em breve..."
        photo_status.color = (
            AppTheme.DARK_TEXT_SECONDARY
            if is_dark_mode
            else AppTheme.LIGHT_TEXT_SECONDARY
        )
        page.update()

    def submit_post(e):
        # Placeholder for post creation logic
        # Future: Send to backend API
        status_text.value = "Post criado com sucesso! ✓"
        status_text.color = AppTheme.SUCCESS
        page.update()

        # Close dialog after 1 second
        import time

        time.sleep(1)
        dialog.open = False
        page.update()

    # Dialog fields
    post_title = AppTheme.get_input_field(
        label="Título",
        hint_text="Ex: Bicicleta usada, Aula de violão...",
        is_dark_mode=is_dark_mode,
        width=AppTheme.CARD_WIDTH_NARROW,
    )

    post_description = AppTheme.get_input_field(
        label="Descrição",
        hint_text="Descreva o que você oferece ou procura",
        is_dark_mode=is_dark_mode,
        width=AppTheme.CARD_WIDTH_NARROW,
        multiline=True,
        min_lines=3,
        max_lines=5,
    )

    # Photo upload placeholder
    photo_status = ft.Text("", size=AppTheme.FONT_SIZE_CAPTION, italic=True)

    add_photos_button = ft.Container(
        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.ADD_PHOTO_ALTERNATE,
                    size=AppTheme.ICON_SIZE_XL,  # 40px
                    color=AppTheme.PRIMARY_GREEN,
                ),
                ft.Text(
                    "Adicionar Fotos",
                    size=AppTheme.FONT_SIZE_BODY,
                    color=AppTheme.PRIMARY_GREEN,
                    weight=AppTheme.FONT_WEIGHT_MEDIUM,
                ),
                photo_status,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=AppTheme.SPACING_SM,
        ),
        on_click=add_photos_placeholder,
        border=ft.border.all(2, AppTheme.PRIMARY_GREEN),
        border_radius=AppTheme.CARD_BORDER_RADIUS,
        padding=AppTheme.SPACING_LG,
        width=AppTheme.CARD_WIDTH_NARROW,
        ink=True,
    )

    status_text = ft.Text("", size=AppTheme.FONT_SIZE_CAPTION)

    # Dialog content
    dialog = ft.AlertDialog(
        title=ft.Text(
            "Criar Nova Publicação",
            size=AppTheme.FONT_SIZE_TITLE,
            weight=AppTheme.FONT_WEIGHT_BOLD,
            color=AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY,
        ),
        content=ft.Column(
            [
                post_title,
                post_description,
                add_photos_button,
                status_text,
            ],
            tight=True,
            spacing=AppTheme.SPACING_MD,
        ),
        actions=[
            AppTheme.get_text_button("Cancelar", close_dialog, is_dark_mode),
            AppTheme.get_elevated_button("Publicar", submit_post, is_dark_mode),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
    )

    page.overlay.append(dialog)
    dialog.open = True
    page.update()
