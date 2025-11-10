"""Reusable AppBar component for post-login pages.

Provides consistent header with app branding and action icons.
"""

import flet as ft
from flet import padding as pd


def create_app_bar() -> ft.Container:
    """Create reusable AppBar with search and notifications icons.

    Returns
    -------
    ft.Container
        Styled top bar container with action buttons
    """
    action_buttons = ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.SEARCH,
                icon_color="#4CAF50",
                icon_size=28,
                tooltip="Buscar",
            ),
            ft.IconButton(
                icon=ft.Icons.NOTIFICATIONS,
                icon_color="#4CAF50",
                icon_size=28,
                tooltip="Notificações",
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    width=450,
                    content=action_buttons,
                    alignment=ft.alignment.center,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=pd.only(top=8, left=0, right=0, bottom=4),
    )

    return top_bar
