"""Reusable NavigationBar component for post-login pages.

Provides consistent bottom navigation across dashboard and profile pages.
"""

import flet as ft
from .new_post_dialog import open_new_post_dialog


def create_nav_bar(page: ft.Page, selected_index: int = 0) -> ft.NavigationBar:
    """Create reusable bottom NavigationBar with three destinations.

    Parameters
    ----------
    page : ft.Page
        Flet page instance for navigation handling
    selected_index : int, optional
        Index of the currently selected tab (0=Dashboard, 1=Novo, 2=Profile)
        Default is 0 (Dashboard)

    Returns
    -------
    ft.NavigationBar
        Styled navigation bar with three destinations
    """

    def on_nav_change(e):
        """Handle navigation between pages."""
        selected = e.control.selected_index

        if selected == 0:  # Início
            from ..pages.dashboard import dashboard

            page.clean()
            dashboard(page)
        elif selected == 1:  # Novo
            # Open new post dialog directly without navigation
            open_new_post_dialog(page)
        elif selected == 2:  # Perfil
            from ..pages.perfil import perfil

            page.clean()
            perfil(page)

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Novo"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        bgcolor="#ffffff",
        indicator_color="#4CAF50",
    )
