import flet as ft
from flet import padding as pd
from ..widgets.new_post_dialog import open_new_post_dialog
from ..widgets.post_card import PostCard
from mock.posts import get_mock_posts


def dashboard(page: ft.Page):
    page.title = "Página inicial - Scambo"
    page.bgcolor = "#f5f5f5"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

    # Navigation handler for bottom bar
    def on_nav_change(e):
        selected_index = e.control.selected_index

        if selected_index == 0:  # Início
            page.clean()
            dashboard(page)
        elif selected_index == 1:  # Novo
            # Open new post dialog directly without navigation
            open_new_post_dialog(page)
        elif selected_index == 2:  # Perfil
            from .perfil import perfil

            page.clean()
            perfil(page)

    # Get sample feed data from mock module (easy to swap for real API later)
    mock_posts = get_mock_posts()

    feed_cards = []
    for mp in mock_posts:
        avatar = ft.CircleAvatar(
            bgcolor=mp["avatar_bg"], content=ft.Text(mp["avatar_text"], color="white")
        )
        feed_cards.append(
            ft.Container(
                alignment=ft.alignment.center,
                content=PostCard(
                    author_name=mp["author_name"],
                    author_avatar=avatar,
                    post_title=mp["post_title"],
                    post_description=mp["post_description"],
                    post_date=mp["post_date"],
                    width=450,
                ),
            )
        )

    # Build a full-screen feed; list will take remaining space and scroll
    feed_list = ft.ListView(
        controls=feed_cards,
        expand=1,
        spacing=12,
        padding=16,
        auto_scroll=False,
    )

    # Action buttons row
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
        content=ft.Row([
            ft.Container(width=450, content=action_buttons, alignment=ft.alignment.center)
        ], alignment=ft.MainAxisAlignment.CENTER),
        padding=pd.only(top=8, left=0, right=0, bottom=4),
    )

    # Footer navigation bar
    nav = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Novo"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        bgcolor="#ffffff",
        indicator_color="#4CAF50",
    )

    # Main layout: top actions, expandable feed, bottom navigation
    page.add(
        ft.Column(
            [
                top_bar,
                feed_list,
                nav,
            ],
            expand=True,
            spacing=0,
        )
    )
