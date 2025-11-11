"""Reusable NavigationBar component for post-login pages.

Provides consistent bottom navigation across dashboard and profile pages.
"""

import flet as ft
from .new_post_dialog import open_new_post_dialog
from mock.notifications import get_mock_notifications_count
from ..theme import AppTheme


def create_nav_bar(
    page: ft.Page, selected_index: int = 0, is_dark_mode: bool = False
) -> ft.NavigationBar:
    """Create reusable bottom NavigationBar with five destinations.

    Parameters
    ----------
    page : ft.Page
        Flet page instance for navigation handling
    selected_index : int, optional
        Index of the currently selected tab (0=Início, 1=Novo, 2=Perfil, 3=Buscar, 4=Notificações)
        Default is 0 (Início)
    is_dark_mode : bool, optional
        Whether to use dark theme styling

    Returns
    -------
    ft.NavigationBar
        Styled navigation bar with five destinations including notifications badge
    """

    def on_nav_change(e):
        """Handle navigation between pages."""
        selected = e.control.selected_index

        if selected == 0:  # Início
            from ..pages.dashboard import dashboard

            page.clean()
            dashboard(page, is_dark_mode)
        elif selected == 1:  # Novo
            # Open new post dialog directly without navigation
            open_new_post_dialog(page, is_dark_mode)
        elif selected == 2:  # Perfil
            from ..pages.perfil import perfil

            page.clean()
            perfil(page, is_dark_mode)
        elif selected == 3:  # Buscar
            # TODO: Implement search functionality
            pass
        elif selected == 4:  # Notificações
            # TODO: Implement notifications page
            pass

    # Get notifications count for badge
    notifications_count = get_mock_notifications_count()

    # Create notifications icon with badge using Stack
    notifications_icon = ft.Stack(
        [
            ft.Icon(ft.Icons.NOTIFICATIONS_OUTLINED),
            (
                ft.Container(
                    content=ft.Text(
                        str(notifications_count),
                        size=AppTheme.FONT_SIZE_SMALL,
                        color="white",
                        weight=AppTheme.FONT_WEIGHT_BOLD,
                    ),
                    bgcolor=AppTheme.ERROR,
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.symmetric(horizontal=5, vertical=2),
                    alignment=ft.alignment.center,
                    top=0,
                    right=0,
                )
                if notifications_count > 0
                else ft.Container()
            ),
        ],
        width=AppTheme.BADGE_SIZE,
        height=AppTheme.BADGE_SIZE,
    )

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Novo"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Buscar"),
            ft.NavigationBarDestination(icon=notifications_icon, label="Notificações"),
        ],
        bgcolor=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
        indicator_color=AppTheme.PRIMARY_GREEN,
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_SHOW,
    )
