"""Notifications page with list of user notifications.

Displays notifications grouped by read/unread status with:
- Scrollable list view
- Pull-to-refresh (placeholder for future implementation)
- Tap to open detail modal
- Mark all as read action
- Notification badge updates
- Theme-aware styling

All styling uses theme.py constants for consistency.
"""

import flet as ft
from ..widgets.nav_bar import create_nav_bar
from ..widgets.notification_card import NotificationCard
from ..widgets.notification_detail_dialog import open_notification_detail_dialog
from ..theme import AppTheme
from mock.notifications import (
    get_mock_notifications,
    mark_notification_as_read,
)


def notifications(page: ft.Page, is_dark_mode: bool = False):
    """
    Notifications page with grouped list and detail modal.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """
    page.title = "Notificações - Scambo"
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

    # State management
    notifications_data = get_mock_notifications()

    def refresh_notifications():
        """Reload notifications from data source."""
        nonlocal notifications_data
        notifications_data = get_mock_notifications()
        build_notification_list()
        page.update()

    def on_notification_click(e):
        """Handle notification card click - open detail modal."""
        notification_id = e.control.data

        # Find notification data
        notification = next(
            (n for n in notifications_data if n["id"] == notification_id), None
        )

        if notification:
            open_notification_detail_dialog(
                page=page,
                notification_data=notification,
                on_mark_read=handle_mark_as_read,
                is_dark_mode=is_dark_mode,
            )

    def handle_mark_as_read(notification_id: int):
        """Mark notification as read and update UI."""
        # Call mock function (will be API call in production)
        success = mark_notification_as_read(notification_id)

        if success:
            # Update local state
            for notification in notifications_data:
                if notification["id"] == notification_id:
                    notification["read"] = True
                    break

            # Rebuild list to reflect changes
            refresh_notifications()

    def handle_mark_all_read(_):
        """Mark all unread notifications as read."""
        unread_count = sum(1 for n in notifications_data if not n["read"])

        if unread_count == 0:
            # Show feedback if no unread notifications
            status_snackbar = ft.SnackBar(
                content=ft.Text("Não há notificações não lidas"),
                bgcolor=AppTheme.INFO,
            )
            page.overlay.append(status_snackbar)
            status_snackbar.open = True
            page.update()
            return

        # Mark all as read
        for notification in notifications_data:
            if not notification["read"]:
                notification["read"] = True
                mark_notification_as_read(notification["id"])

        # Show success feedback
        success_snackbar = ft.SnackBar(
            content=ft.Text(f"{unread_count} notificações marcadas como lidas"),
            bgcolor=AppTheme.SUCCESS,
        )
        page.overlay.append(success_snackbar)
        success_snackbar.open = True

        # Refresh list
        refresh_notifications()

    def build_notification_list():
        """Build the notification list with grouping."""
        # Separate unread and read notifications
        unread = [n for n in notifications_data if not n["read"]]
        read = [n for n in notifications_data if n["read"]]

        # Build notification cards
        notification_cards = []

        # Unread section
        if unread:
            notification_cards.append(
                ft.Container(
                    content=ft.Text(
                        f"Não lidas ({len(unread)})",
                        size=AppTheme.FONT_SIZE_SUBTITLE,
                        weight=AppTheme.FONT_WEIGHT_BOLD,
                        color=(
                            AppTheme.DARK_TEXT_PRIMARY
                            if is_dark_mode
                            else AppTheme.LIGHT_TEXT_PRIMARY
                        ),
                    ),
                    padding=ft.padding.only(
                        top=AppTheme.SPACING_MD,
                        bottom=AppTheme.SPACING_SM,
                    ),
                )
            )

            for notification in unread:
                notification_cards.append(
                    NotificationCard(
                        notification_id=notification["id"],
                        notification_type=notification["type"],
                        message=notification["message"],
                        timestamp=notification["timestamp"],
                        is_read=notification["read"],
                        avatar_bg=notification.get("sender_avatar_bg"),
                        avatar_text=notification.get("sender_avatar_text"),
                        on_click=on_notification_click,
                        is_dark_mode=is_dark_mode,
                    )
                )

        # Read section
        if read:
            notification_cards.append(
                ft.Container(
                    content=ft.Text(
                        "Anteriores",
                        size=AppTheme.FONT_SIZE_SUBTITLE,
                        weight=AppTheme.FONT_WEIGHT_BOLD,
                        color=(
                            AppTheme.DARK_TEXT_PRIMARY
                            if is_dark_mode
                            else AppTheme.LIGHT_TEXT_PRIMARY
                        ),
                    ),
                    padding=ft.padding.only(
                        top=AppTheme.SPACING_LG,
                        bottom=AppTheme.SPACING_SM,
                    ),
                )
            )

            for notification in read:
                notification_cards.append(
                    NotificationCard(
                        notification_id=notification["id"],
                        notification_type=notification["type"],
                        message=notification["message"],
                        timestamp=notification["timestamp"],
                        is_read=notification["read"],
                        avatar_bg=notification.get("sender_avatar_bg"),
                        avatar_text=notification.get("sender_avatar_text"),
                        on_click=on_notification_click,
                        is_dark_mode=is_dark_mode,
                    )
                )

        # Empty state
        if not unread and not read:
            notification_cards.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(
                                ft.Icons.NOTIFICATIONS_NONE,
                                size=AppTheme.ICON_SIZE_XL * 2,  # 80px empty state icon
                                color=(
                                    AppTheme.DARK_TEXT_TERTIARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_TERTIARY
                                ),
                            ),
                            ft.Text(
                                "Nenhuma notificação",
                                size=AppTheme.FONT_SIZE_SUBTITLE,
                                color=(
                                    AppTheme.DARK_TEXT_SECONDARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_SECONDARY
                                ),
                            ),
                            ft.Text(
                                "Você está em dia! 🎉",
                                size=AppTheme.FONT_SIZE_BODY,
                                color=(
                                    AppTheme.DARK_TEXT_TERTIARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_TERTIARY
                                ),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=AppTheme.SPACING_MD,
                    ),
                    alignment=ft.Alignment.CENTER,
                    expand=True,
                )
            )

        # Update list view
        notifications_list.controls = notification_cards

        # Only call update if the control is already attached to a page.
        # Accessing `control.page` raises RuntimeError when the control is not
        # added, so guard with try/except to avoid the 'Control must be added'
        # runtime error during initial build before `page.add()` is called.
        try:
            _ = notifications_list.page
        except RuntimeError:
            # Not yet attached to page; skip update for now.
            pass
        else:
            notifications_list.update()

    # Page header with title and actions
    header = ft.Row(
        [
            ft.Text(
                "Notificações",
                size=AppTheme.FONT_SIZE_TITLE,
                weight=AppTheme.FONT_WEIGHT_BOLD,
                color=(
                    AppTheme.DARK_TEXT_PRIMARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_PRIMARY
                ),
            ),
            ft.Row(
                [
                    # Refresh button (placeholder for pull-to-refresh)
                    ft.IconButton(
                        icon=ft.Icons.REFRESH,
                        tooltip="Atualizar",
                        icon_color=AppTheme.PRIMARY_GREEN,
                        on_click=lambda e: refresh_notifications(),
                    ),
                    # Mark all as read button
                    ft.IconButton(
                        icon=ft.Icons.DONE_ALL,
                        tooltip="Marcar todas como lidas",
                        icon_color=AppTheme.PRIMARY_GREEN,
                        on_click=handle_mark_all_read,
                    ),
                ],
                spacing=0,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Notifications list view (constrained width for consistency)
    notifications_list = ft.ListView(
        controls=[],
        expand=True,
        spacing=AppTheme.SPACING_SM,
        padding=0,
        auto_scroll=False,
    )

    # Initial list build
    build_notification_list()

    # Content container with centered, constrained width (matches other pages)
    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Container(height=AppTheme.SPACING_LG),
                header,
                ft.Container(height=AppTheme.SPACING_MD),
                AppTheme.get_divider(is_dark_mode),
                notifications_list,
            ],
            spacing=0,
            scroll=ft.ScrollMode.HIDDEN,
        ),
        width=AppTheme.CARD_WIDTH_STANDARD,  # 450px - matches dashboard cards
        expand=True,
    )

    # Get navigation bar
    nav = create_nav_bar(page, selected_index=4, is_dark_mode=is_dark_mode)

    # Main layout with centered content
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=content_container,
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                ),
                nav,
            ],
            expand=True,
            spacing=0,
        )
    )


if __name__ == "__main__":
    ft.app(target=notifications)
