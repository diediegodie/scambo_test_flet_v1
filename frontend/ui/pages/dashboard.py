import flet as ft
from ..widgets.new_post_dialog import open_new_post_dialog
from ..widgets.post_card import PostCard
from ..widgets.app_bar import create_app_bar
from ..widgets.nav_bar import create_nav_bar
from mock.posts import get_mock_posts


def dashboard(page: ft.Page):
    page.title = "Página inicial - Scambo"
    page.bgcolor = "#f5f5f5"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

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

    # Get reusable components
    top_bar = create_app_bar()
    nav = create_nav_bar(page, selected_index=0)

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
