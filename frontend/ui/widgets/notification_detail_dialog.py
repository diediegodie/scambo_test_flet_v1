"""Notification detail dialog component.

Displays full notification information in a modal dialog:
- Complete message with sender details
- Full timestamp
- Related content preview (if applicable)
- Mark as read action
- Close button

Follows the same pattern as new_post_dialog.py for consistency.
"""

import flet as ft
from typing import Callable
from ..theme import AppTheme


def open_notification_detail_dialog(
    page: ft.Page,
    notification_data: dict,
    on_mark_read: Callable,
    is_dark_mode: bool = False,
):
    """
    Opens notification detail dialog with full information.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    notification_data : dict
        Complete notification data with keys:
        - id: int
        - type: str (comment, like, new_post)
        - message: str
        - timestamp: str
        - read: bool
        - sender_name: str (optional)
        - sender_avatar_bg: str (optional)
        - sender_avatar_text: str (optional)
        - related_content: str (optional)
        - related_image: str (optional)
    on_mark_read : Callable
        Callback to mark notification as read (receives notification_id)
    is_dark_mode : bool
        Whether to use dark theme styling
    """

    # Fixed dialog width to match dashboard feed (CARD_WIDTH_STANDARD = 450px)
    dialog_width = AppTheme.CARD_WIDTH_STANDARD
    # Content height: leave room for title, actions, and padding
    content_max_height = 500

    notification_id = notification_data.get("id")
    notification_type = notification_data.get("type", "system")
    message = notification_data.get("message", "")
    timestamp = notification_data.get("timestamp", "")
    is_read = notification_data.get("read", False)
    sender_name = notification_data.get("sender_name", "")
    sender_avatar_bg = notification_data.get(
        "sender_avatar_bg", AppTheme.DEFAULT_AVATAR_BG
    )
    sender_avatar_text = notification_data.get("sender_avatar_text", "?")
    related_content = notification_data.get("related_content")
    related_image = notification_data.get("related_image")

    # Type icon mapping
    type_icons = {
        "comment": (ft.Icons.CHAT_BUBBLE, AppTheme.INFO, "Comentário"),
        "like": (ft.Icons.FAVORITE, AppTheme.ERROR, "Curtida"),
        "new_post": (ft.Icons.ARTICLE, AppTheme.PRIMARY_GREEN, "Nova Publicação"),
        "system": (ft.Icons.INFO, AppTheme.WARNING, "Sistema"),
    }

    icon_name, icon_color, type_label = type_icons.get(
        notification_type,
        (ft.Icons.NOTIFICATIONS, AppTheme.PRIMARY_GREEN, "Notificação"),
    )

    def close_dialog(_):
        """Close dialog handler."""
        dialog.open = False
        page.update()

    def mark_as_read_handler(_):
        """Mark notification as read and close dialog."""
        # Call the callback to update notification state
        on_mark_read(notification_id)

        # Update status text
        status_text.value = "✓ Marcada como lida"
        status_text.color = AppTheme.SUCCESS
        page.update()

        # Close dialog after brief delay
        import time

        time.sleep(0.5)
        dialog.open = False
        page.update()

    # Build sender section
    sender_section = None
    if sender_name:
        sender_avatar = ft.CircleAvatar(
            bgcolor=sender_avatar_bg,
            content=ft.Text(
                sender_avatar_text,
                color=AppTheme.TEXT_ON_COLORED_BG,
                size=AppTheme.ICON_SIZE_LG,
                weight=AppTheme.FONT_WEIGHT_BOLD,
            ),
            radius=AppTheme.AVATAR_RADIUS_LARGE,
        )

        sender_section = ft.Row(
            [
                sender_avatar,
                ft.Column(
                    [
                        ft.Text(
                            sender_name,
                            size=AppTheme.FONT_SIZE_SUBTITLE,
                            weight=AppTheme.FONT_WEIGHT_BOLD,
                            color=(
                                AppTheme.DARK_TEXT_PRIMARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_PRIMARY
                            ),
                        ),
                        ft.Text(
                            type_label,
                            size=AppTheme.FONT_SIZE_CAPTION,
                            color=(
                                AppTheme.DARK_TEXT_SECONDARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_SECONDARY
                            ),
                        ),
                    ],
                    spacing=AppTheme.SPACING_XS,
                ),
            ],
            spacing=AppTheme.DIALOG_CONTENT_PADDING,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )  # Message section
    message_section = ft.Container(
        content=ft.Text(
            message,
            size=AppTheme.FONT_SIZE_BODY,
            # No max_lines - allow natural text wrapping in scrollable content
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

    # Timestamp section
    timestamp_section = ft.Row(
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
                timestamp,
                size=AppTheme.FONT_SIZE_CAPTION,
                color=(
                    AppTheme.DARK_TEXT_TERTIARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_TERTIARY
                ),
            ),
        ],
        spacing=AppTheme.SPACING_XS,
    )

    # Related content section (if available)
    related_section = None
    if related_content:
        related_widgets = [
            AppTheme.get_divider(is_dark_mode),
            ft.Container(height=AppTheme.SPACING_SM),
            ft.Text(
                "Conteúdo relacionado",
                size=AppTheme.FONT_SIZE_CAPTION,
                weight=AppTheme.FONT_WEIGHT_MEDIUM,
                color=(
                    AppTheme.DARK_TEXT_SECONDARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_SECONDARY
                ),
            ),
        ]

        # Add image if available
        if related_image:
            # Calculate responsive image width (dialog width minus content padding on both sides)
            responsive_image_width = dialog_width - (
                AppTheme.DIALOG_CONTENT_PADDING * 2
            )
            related_widgets.append(
                ft.Container(
                    content=ft.Image(
                        src=related_image,
                        width=responsive_image_width,
                        height=AppTheme.DIALOG_RELATED_IMAGE_HEIGHT,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
                    ),
                    padding=ft.padding.only(
                        top=AppTheme.DIALOG_TITLE_PADDING,
                        bottom=AppTheme.DIALOG_TITLE_PADDING,
                    ),
                )
            )

        # Add related text
        related_widgets.append(
            ft.Text(
                related_content,
                size=AppTheme.FONT_SIZE_BODY,
                color=(
                    AppTheme.DARK_TEXT_SECONDARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_SECONDARY
                ),
                # No max_lines - allow full content to display with scroll
            )
        )

        related_section = ft.Column(
            controls=related_widgets,
            spacing=AppTheme.SPACING_XS,
        )

    # Status text for feedback
    status_text = ft.Text("", size=AppTheme.FONT_SIZE_CAPTION)

    # Build dialog content
    dialog_content_widgets = []

    if sender_section:
        dialog_content_widgets.append(sender_section)

    dialog_content_widgets.extend(
        [
            message_section,
            timestamp_section,
        ]
    )

    if related_section:
        dialog_content_widgets.append(related_section)

    dialog_content_widgets.append(status_text)

    # Build action buttons - use list of Controls
    action_buttons: list[ft.Control] = [
        AppTheme.get_text_button("Fechar", close_dialog, is_dark_mode),
    ]

    # Add "Mark as read" button if not already read
    if not is_read:
        action_buttons.insert(
            0,
            AppTheme.get_elevated_button(
                "Marcar como lida",
                mark_as_read_handler,
                is_dark_mode,
            ),
        )

    # Create dialog
    dialog = ft.AlertDialog(
        title=ft.Row(
            [
                ft.Icon(icon_name, color=icon_color, size=AppTheme.ICON_SIZE_LG),
                ft.Text(
                    "Detalhes da Notificação",
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
