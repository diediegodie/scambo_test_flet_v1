# When wire the backend:
# Replace mock.user.get_current_user() with an async API call
# Add JWT token handling in core/ for authenticated requests
# Define a UserSchema in schemas/user.py for validation

import flet as ft
from ..widgets.new_post_dialog import open_new_post_dialog
from ..widgets.app_bar import create_app_bar
from ..widgets.nav_bar import create_nav_bar
from mock.user import get_current_user
from mock.posts import count_user_posts


def perfil(page: ft.Page):
    """Professional user profile page with avatar, bio, stats, and actions."""
    page.title = "Perfil - Scambo"
    page.bgcolor = "#f5f5f5"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

    # Get current user data from mock module (easy to swap for real API later)
    user = get_current_user()
    user_posts_count = count_user_posts(user["name"])

    # Profile header with avatar and user info
    profile_header = ft.Column(
        [
            ft.CircleAvatar(
                bgcolor=user["avatar_bg"],
                content=ft.Text(
                    user["avatar_text"],
                    color="white",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=50,
            ),
            ft.Text(
                user["name"],
                size=28,
                weight=ft.FontWeight.BOLD,
                color="#333333",
            ),
            ft.Text(
                user["email"],
                size=14,
                color="#777777",
            ),
            # Bio section
            ft.Container(
                content=ft.Text(
                    user["bio"],
                    size=14,
                    color="#555555",
                    text_align=ft.TextAlign.CENTER,
                ),
                width=400,
                padding=ft.padding.only(top=10),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8,
    )

    # Stats section with counters
    stats_row = ft.Row(
        [
            # Publications counter
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.Icons.ARTICLE_OUTLINED,
                                    color="#4CAF50",
                                    size=24,
                                ),
                                ft.Text(
                                    str(user_posts_count),
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="#333333",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,
                        ),
                        ft.Text(
                            "Publicações",
                            size=12,
                            color="#777777",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=15,
                border_radius=8,
                bgcolor="#ffffff",
                expand=True,
            ),
            # Reputation counter
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.Icons.STAR,
                                    color="#FF9800",
                                    size=24,
                                ),
                                ft.Text(
                                    f"{user['reputation']:.1f}",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="#333333",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,
                        ),
                        ft.Text(
                            "Reputação",
                            size=12,
                            color="#777777",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=15,
                border_radius=8,
                bgcolor="#ffffff",
                expand=True,
            ),
        ],
        spacing=15,
        width=400,
    )

    # "Nova publicação" button
    novo_button = ft.ElevatedButton(
        "Nova publicação",
        icon=ft.Icons.ADD,
        bgcolor="#4CAF50",
        color="white",
        on_click=lambda e: open_new_post_dialog(page),
        width=400,
        height=50,
    )

    # Main content card (centered like login/create account)
    content_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    profile_header,
                    ft.Divider(height=20, color="#eeeeee"),
                    stats_row,
                    novo_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=40,
            width=500,
        ),
        elevation=4,
    )

    # Get reusable components
    top_bar = create_app_bar()
    nav = create_nav_bar(page, selected_index=2)  # Profile is selected

    # Main layout with top bar, centered content, and bottom navigation
    page.add(
        ft.Column(
            [
                top_bar,
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
