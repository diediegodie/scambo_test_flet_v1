"""Post detail dialog component.

Displays full post information in a modal dialog:
- Post title and author details
- Post image (if available)
- Full description
- Tags
- Post date
- Close button

Follows the same pattern as notification_detail_dialog.py for consistency.
Designed for use in search page and other post discovery flows.
"""

import flet as ft
from ..theme import AppTheme


def open_post_detail_dialog(
    page: ft.Page,
    post_data: dict,
    is_dark_mode: bool = False,
):
    """
    Opens post detail dialog with full information.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    post_data : dict
        Complete post data with keys:
        - post_title: str
        - post_description: str
        - author_name: str
        - avatar_bg: str
        - avatar_text: str
        - post_date: str
        - tags: list[str]
        - image_path: str (optional)
    is_dark_mode : bool
        Whether to use dark theme styling
    """

    # Fixed dialog width to match dashboard feed (CARD_WIDTH_STANDARD = 450px)
    dialog_width = AppTheme.CARD_WIDTH_STANDARD
    # Content height: leave room for title, actions, and padding
    content_max_height = 500

    post_title = post_data.get("post_title", "")
    post_description = post_data.get("post_description", "")
    author_name = post_data.get("author_name", "")
    avatar_bg = post_data.get("avatar_bg", AppTheme.DEFAULT_AVATAR_BG)
    avatar_text = post_data.get("avatar_text", "?")
    post_date = post_data.get("post_date", "")
    tags = post_data.get("tags", [])
    image_path = post_data.get("image_path")

    def close_dialog(_):
        """Close dialog handler."""
        dialog.open = False
        page.update()

    # Author section with avatar
    author_avatar = ft.CircleAvatar(
        bgcolor=avatar_bg,
        content=ft.Text(
            avatar_text,
            color=AppTheme.TEXT_ON_COLORED_BG,
            size=AppTheme.ICON_SIZE_LG,
            weight=AppTheme.FONT_WEIGHT_BOLD,
        ),
        radius=AppTheme.AVATAR_RADIUS_LARGE,
    )

    author_section = ft.Row(
        [
            author_avatar,
            ft.Column(
                [
                    ft.Text(
                        author_name,
                        size=AppTheme.FONT_SIZE_SUBTITLE,
                        weight=AppTheme.FONT_WEIGHT_BOLD,
                        color=(
                            AppTheme.DARK_TEXT_PRIMARY
                            if is_dark_mode
                            else AppTheme.LIGHT_TEXT_PRIMARY
                        ),
                    ),
                    ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.ACCESS_TIME,
                                size=AppTheme.ICON_SIZE_SM,
                                color=(
                                    AppTheme.DARK_TEXT_TERTIARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_TERTIARY
                                ),
                            ),
                            ft.Text(
                                post_date,
                                size=AppTheme.FONT_SIZE_CAPTION,
                                color=(
                                    AppTheme.DARK_TEXT_TERTIARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_TERTIARY
                                ),
                            ),
                        ],
                        spacing=AppTheme.SPACING_XS,
                    ),
                ],
                spacing=AppTheme.SPACING_XS,
            ),
        ],
        spacing=AppTheme.DIALOG_CONTENT_PADDING,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Title section
    title_section = ft.Container(
        content=ft.Text(
            post_title,
            size=AppTheme.FONT_SIZE_TITLE,
            weight=AppTheme.FONT_WEIGHT_BOLD,
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
        ),
        padding=ft.padding.only(
            top=AppTheme.DIALOG_CONTENT_PADDING,
            bottom=AppTheme.DIALOG_TITLE_PADDING,
        ),
    )

    # Image section (if available)
    image_section = None
    if image_path:
        # Calculate responsive image width (dialog width minus padding)
        responsive_image_width = dialog_width - (AppTheme.DIALOG_CONTENT_PADDING * 2)

        image_section = ft.Container(
            content=ft.Image(
                src=image_path,
                width=responsive_image_width,
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
                error_content=ft.Icon(
                    ft.Icons.BROKEN_IMAGE,
                    size=AppTheme.ICON_SIZE_XL,
                    color=(
                        AppTheme.DARK_TEXT_TERTIARY
                        if is_dark_mode
                        else AppTheme.LIGHT_TEXT_TERTIARY
                    ),
                ),
            ),
            height=AppTheme.DIALOG_IMAGE_HEIGHT,
            bgcolor=(
                AppTheme.DARK_SURFACE_VARIANT
                if is_dark_mode
                else AppTheme.LIGHT_SURFACE_VARIANT
            ),
            border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
            padding=ft.padding.only(
                top=AppTheme.DIALOG_TITLE_PADDING,
                bottom=AppTheme.DIALOG_CONTENT_PADDING,
            ),
        )

    # Description section
    description_section = ft.Container(
        content=ft.Text(
            post_description,
            size=AppTheme.FONT_SIZE_BODY,
            # No max_lines - allow natural text wrapping in scrollable content
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
        ),
        padding=ft.padding.only(bottom=AppTheme.DIALOG_CONTENT_PADDING),
    )

    # Tags section (if available)
    tags_section = None
    if tags:
        tag_chips = []
        for tag in tags:
            tag_chips.append(
                ft.Container(
                    content=ft.Text(
                        f"#{tag}",
                        size=AppTheme.FONT_SIZE_SMALL,
                        color=AppTheme.TEXT_ON_COLORED_BG,
                        weight=AppTheme.FONT_WEIGHT_MEDIUM,
                    ),
                    bgcolor=AppTheme.PRIMARY_GREEN,
                    padding=ft.padding.symmetric(
                        horizontal=AppTheme.DIALOG_TITLE_PADDING,
                        vertical=AppTheme.SPACING_XS,
                    ),
                    border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
                )
            )

        tags_section = ft.Container(
            content=ft.Row(
                tag_chips,
                spacing=AppTheme.SPACING_XS,
                wrap=True,
            ),
            padding=ft.padding.only(bottom=AppTheme.DIALOG_CONTENT_PADDING),
        )

    # Build dialog content widgets
    dialog_content_widgets = [
        author_section,
        title_section,
    ]

    if image_section:
        dialog_content_widgets.append(image_section)

    dialog_content_widgets.append(description_section)

    if tags_section:
        dialog_content_widgets.append(tags_section)

    # Build action buttons - use list of Controls (matches notification dialog pattern)
    action_buttons: list[ft.Control] = [
        AppTheme.get_text_button("Fechar", close_dialog, is_dark_mode),
    ]

    # Create dialog (structure matches notification_detail_dialog.py)
    dialog = ft.AlertDialog(
        title=ft.Row(
            [
                ft.Icon(
                    ft.Icons.ARTICLE,
                    size=AppTheme.ICON_SIZE_LG,
                    color=AppTheme.PRIMARY_GREEN,
                ),
                ft.Text(
                    "Detalhes da Publicação",
                    size=AppTheme.FONT_SIZE_TITLE,
                    weight=AppTheme.FONT_WEIGHT_BOLD,
                    color=(
                        AppTheme.DARK_TEXT_PRIMARY
                        if is_dark_mode
                        else AppTheme.LIGHT_TEXT_PRIMARY
                    ),
                ),
            ],
            spacing=AppTheme.DIALOG_TITLE_PADDING,
        ),
        content=ft.Container(
            content=ft.Column(
                controls=dialog_content_widgets,
                tight=True,
                spacing=AppTheme.DIALOG_TITLE_PADDING,
                scroll=ft.ScrollMode.AUTO,
                height=content_max_height,
            ),
            width=dialog_width,
            padding=AppTheme.DIALOG_CONTENT_PADDING,  # Standardized content padding
        ),
        actions=action_buttons,
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
        modal=True,
    )

    # Show dialog
    page.overlay.append(dialog)
    dialog.open = True
    page.update()
