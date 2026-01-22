"""Reusable NotificationCard widget for notification list.

This component displays individual notifications with:
- Avatar with dynamic background color
- Notification type icon (comment, like, new_post)
- Message text with sender name
- Timestamp
- Read/unread visual state
- Tap handler for opening detail modal

Use only from notifications page. All styling uses theme.py constants.
"""

import flet as ft
from typing import Callable
from ..theme import AppTheme


def NotificationCard(
    notification_id: int,
    notification_type: str,
    message: str,
    timestamp: str,
    is_read: bool,
    avatar_bg: str | None = None,
    avatar_text: str | None = None,
    on_click: Callable | None = None,
    is_dark_mode: bool = False,
) -> ft.Container:
    """Return a styled notification card.

    Parameters
    ----------
    notification_id : int
        Unique notification identifier
    notification_type : str
        Type of notification: "comment", "like", "new_post"
    message : str
        Notification message text
    timestamp : str
        Human-readable timestamp (e.g., "Há 5 minutos")
    is_read : bool
        Whether notification has been read
    avatar_bg : str | None
        Avatar background color (hex). Uses default if None.
    avatar_text : str | None
        Avatar text (usually first letter of name). Uses "?" if None.
    on_click : Callable | None
        Callback when notification is tapped
    is_dark_mode : bool
        Whether to apply dark theme styling
    """

    # Icon mapping based on notification type
    type_icons = {
        "comment": (ft.Icons.CHAT_BUBBLE, AppTheme.INFO),
        "like": (ft.Icons.FAVORITE, AppTheme.ERROR),
        "new_post": (ft.Icons.ARTICLE, AppTheme.PRIMARY_GREEN),
        "system": (ft.Icons.INFO, AppTheme.WARNING),
    }

    icon_name, icon_color = type_icons.get(
        notification_type, (ft.Icons.NOTIFICATIONS, AppTheme.PRIMARY_GREEN)
    )

    # Avatar configuration
    avatar_bg_color = avatar_bg or AppTheme.DEFAULT_AVATAR_BG
    avatar_text_content = avatar_text or "?"

    # Read/unread styling
    if is_read:
        # Read notifications have subtle, semi-transparent appearance
        card_bgcolor = (
            AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
        )
        text_weight = AppTheme.FONT_WEIGHT_NORMAL
        opacity = 0.7
    else:
        # Unread notifications are more prominent
        card_bgcolor = AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE
        text_weight = AppTheme.FONT_WEIGHT_MEDIUM
        opacity = 1.0

    # Build avatar
    avatar = ft.CircleAvatar(
        bgcolor=avatar_bg_color,
        content=ft.Text(
            avatar_text_content,
            color=AppTheme.TEXT_ON_COLORED_BG,
            size=AppTheme.FONT_SIZE_BODY,
            weight=AppTheme.FONT_WEIGHT_BOLD,
        ),
        radius=AppTheme.AVATAR_RADIUS_SMALL,
    )

    # Notification icon
    notification_icon = ft.Icon(
        icon_name,
        color=icon_color,
        size=AppTheme.ICON_SIZE_MD,
    )

    # Message text
    message_text = ft.Text(
        message,
        size=AppTheme.FONT_SIZE_BODY,
        weight=text_weight,
        color=(
            AppTheme.DARK_TEXT_PRIMARY if is_dark_mode else AppTheme.LIGHT_TEXT_PRIMARY
        ),
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
    )

    # Timestamp text
    timestamp_text = ft.Text(
        timestamp,
        size=AppTheme.FONT_SIZE_CAPTION,
        color=(
            AppTheme.DARK_TEXT_TERTIARY
            if is_dark_mode
            else AppTheme.LIGHT_TEXT_TERTIARY
        ),
    )

    # Unread indicator dot
    unread_dot = (
        ft.Container(
            width=AppTheme.SPACING_SM,
            height=AppTheme.SPACING_SM,
            border_radius=AppTheme.SPACING_SM // 2,
            bgcolor=AppTheme.PRIMARY_GREEN,
        )
        if not is_read
        else ft.Container(width=AppTheme.SPACING_SM)
    )

    # Main content layout
    content = ft.Row(
        [
            avatar,
            ft.Column(
                [
                    ft.Row(
                        [
                            notification_icon,
                            ft.Container(width=AppTheme.SPACING_XS),
                            message_text,
                        ],
                        spacing=0,
                    ),
                    timestamp_text,
                ],
                spacing=AppTheme.SPACING_XS,
                expand=True,
            ),
            unread_dot,
        ],
        spacing=AppTheme.SPACING_MD,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    # Return interactive container
    return ft.Container(
        content=content,
        bgcolor=card_bgcolor,
        border_radius=AppTheme.CARD_BORDER_RADIUS,
        padding=AppTheme.SPACING_MD,
        opacity=opacity,
        on_click=on_click,
        ink=True,  # Material ripple effect on tap
        animate_opacity=300,  # Smooth opacity transitions
        data=notification_id,  # Store ID for event handlers
    )
