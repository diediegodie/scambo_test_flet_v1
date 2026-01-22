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

    # Fixed dialog width to match dashboard feed (CARD_WIDTH_STANDARD = 450px)
    dialog_width = AppTheme.CARD_WIDTH_STANDARD
    # Content height: leave room for title, actions, and padding
    content_max_height = 400

    def close_dialog(_):
        dialog.open = False
        page.update()
        # Restore previous keyboard handler if any
        page.on_keyboard_event = previous_keyboard_handler

    def add_photos_placeholder(_):
        # Placeholder for future photo upload functionality
        photo_status.value = "📸 Função de adicionar fotos em breve..."
        photo_status.color = (
            AppTheme.DARK_TEXT_SECONDARY
            if is_dark_mode
            else AppTheme.LIGHT_TEXT_SECONDARY
        )
        page.update()

    def submit_post(_):
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

    # Dialog fields - stretch to full dialog width (minus content padding)
    field_width = dialog_width - (AppTheme.DIALOG_CONTENT_PADDING * 2)

    post_title = AppTheme.get_input_field(
        label="Título",
        hint_text="Ex: Bicicleta usada, Aula de violão...",
        is_dark_mode=is_dark_mode,
        width=field_width,
    )

    post_description = AppTheme.get_input_field(
        label="Descrição",
        hint_text="Descreva o que você oferece ou procura",
        is_dark_mode=is_dark_mode,
        width=field_width,
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
        border=ft.border.all(AppTheme.BORDER_WIDTH_STANDARD, AppTheme.PRIMARY_GREEN),
        border_radius=AppTheme.CARD_BORDER_RADIUS,
        padding=AppTheme.DIALOG_INSET_PADDING,  # Use standardized dialog padding
        width=field_width,  # Match input field width for consistency
        ink=True,
    )

    status_text = ft.Text("", size=AppTheme.FONT_SIZE_CAPTION)

    # Dialog content
    dialog = ft.AlertDialog(
        title=ft.Text(
            "Criar Nova Publicação",
            size=AppTheme.FONT_SIZE_TITLE,
            weight=AppTheme.FONT_WEIGHT_BOLD,
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
        ),
        content=ft.Container(
            content=ft.Column(
                [
                    post_title,
                    post_description,
                    add_photos_button,
                    status_text,
                ],
                tight=True,
                spacing=AppTheme.DIALOG_CONTENT_PADDING,
                scroll=ft.ScrollMode.AUTO,
                height=content_max_height,
            ),
            width=dialog_width,
            padding=AppTheme.DIALOG_CONTENT_PADDING,  # Standardized content padding
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
    # Temporary keyboard handler to close dialog on Escape
    previous_keyboard_handler = page.on_keyboard_event

    def _escape_handler(e: ft.KeyboardEvent):
        if e.key == "Escape":
            dialog.open = False
            page.update()
            page.on_keyboard_event = previous_keyboard_handler
        elif previous_keyboard_handler:
            # Delegate to previous handler for other keys
            previous_keyboard_handler(e)

    page.on_keyboard_event = _escape_handler
    page.update()
