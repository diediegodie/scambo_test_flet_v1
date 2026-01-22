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
    """Create reusable bottom NavigationBar with six destinations.

    Parameters
    ----------
    page : ft.Page
        Flet page instance for navigation handling
    selected_index : int, optional
        Index of the currently selected tab (0=Início, 1=Novo, 2=Perfil, 3=Buscar, 4=Notificações, 5=Configurações)
        Default is 0 (Início)
    is_dark_mode : bool, optional
        Whether to use dark theme styling

    Returns
    -------
    ft.NavigationBar
        Styled navigation bar with six destinations including notifications badge
    """

    def on_nav_change(e):
        """Handle navigation between pages."""
        selected = e.control.selected_index

        # Get current theme from client storage or use passed value
        current_dark_mode = page.client_storage.get("is_dark_mode")
        if current_dark_mode is None:
            current_dark_mode = is_dark_mode

        if selected == 0:  # Início
            from ..pages.dashboard import dashboard

            page.clean()
            dashboard(page, current_dark_mode)
        elif selected == 1:  # Novo
            # Open new post dialog directly without navigation
            open_new_post_dialog(page, current_dark_mode)
        elif selected == 2:  # Perfil
            from ..pages.perfil import perfil

            page.clean()
            perfil(page, current_dark_mode)
        elif selected == 3:  # Buscar
            from ..pages.search import search

            page.clean()
            search(page, current_dark_mode)
        elif selected == 4:  # Notificações
            from ..pages.notifications import notifications

            page.clean()
            notifications(page, current_dark_mode)
        elif selected == 5:  # Configurações
            from ..pages.configurations import configurations

            page.clean()
            configurations(page, current_dark_mode)

    # Get notifications count for badge
    notifications_count = get_mock_notifications_count()

    # Create notifications icon with badge using Stack
    NOTIFICATIONS_ICON = ft.Stack(
        [
            ft.Icon(ft.Icons.NOTIFICATIONS_OUTLINED),
            (
                ft.Container(
                    content=ft.Text(
                        str(notifications_count),
                        size=AppTheme.FONT_SIZE_SMALL,
                        color=AppTheme.TEXT_ON_COLORED_BG,
                        weight=AppTheme.FONT_WEIGHT_BOLD,
                    ),
                    bgcolor=AppTheme.ERROR,
                    border_radius=ft.border_radius.all(AppTheme.BADGE_BORDER_RADIUS),
                    padding=ft.padding.symmetric(
                        horizontal=AppTheme.BADGE_PADDING_HORIZONTAL,
                        vertical=AppTheme.BADGE_PADDING_VERTICAL,
                    ),
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
            ft.NavigationBarDestination(icon=NOTIFICATIONS_ICON, label="Notificações"),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS_OUTLINED, label="Configurações"
            ),
        ],
        bgcolor=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
        indicator_color=AppTheme.PRIMARY_GREEN,
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_SHOW,
    )
