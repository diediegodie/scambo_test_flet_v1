# When wire the backend:
# Replace mock.user.get_current_user() with an async API call
# Add JWT token handling in core/ for authenticated requests
# Define a UserSchema in schemas/user.py for validation

import flet as ft
from ..widgets.new_post_dialog import open_new_post_dialog
from mock.user import get_current_user


def perfil(page: ft.Page):
    """Minimalistic user profile page with avatar and new post button."""
    page.title = "Perfil - Scambo"
    page.bgcolor = "#f5f5f5"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    # Navigation handler for bottom bar
    def on_nav_change(e):
        selected_index = e.control.selected_index

        if selected_index == 0:  # Início
            from .dashboard import dashboard

            page.clean()
            dashboard(page)
        elif selected_index == 1:  # Novo
            # Open new post dialog directly
            open_new_post_dialog(page)
        elif selected_index == 2:  # Perfil
            page.clean()
            perfil(page)

    # Get current user data from mock module (easy to swap for real API later)
    user = get_current_user()

    # Profile header with user info
    profile_content = ft.Column(
        [
            ft.CircleAvatar(
                bgcolor=user["avatar_bg"],
                content=ft.Text(
                    user["avatar_text"], color="white", size=40, weight=ft.FontWeight.BOLD
                ),
                radius=50,
            ),
            ft.Text(
                user["name"],
                size=24,
                weight=ft.FontWeight.BOLD,
                color="#333333",
            ),
            ft.Text(
                user["email"],
                size=14,
                color="#666666",
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    # "Nova publicação" button
    novo_button = ft.ElevatedButton(
        "Nova publicação",
        icon=ft.Icons.ADD,
        bgcolor="#4CAF50",
        color="white",
        on_click=lambda e: open_new_post_dialog(page),
        width=300,
        height=50,
    )

    # Main content card (centered like login/create account)
    content_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    profile_content,
                    novo_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
            ),
            padding=40,
            width=450,
        ),
        elevation=4,
    )

    # Bottom navigation bar (consistent across pages)
    nav = ft.NavigationBar(
        selected_index=2,  # Profile is selected
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Novo"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        bgcolor="#ffffff",
        indicator_color="#4CAF50",
    )

    # Main layout with centered content
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=content_card,
                    expand=True,
                    alignment=ft.alignment.center,
                ),
                nav,
            ],
            expand=True,
            spacing=0,
        )
    )


if __name__ == "__main__":
    ft.app(target=perfil)
