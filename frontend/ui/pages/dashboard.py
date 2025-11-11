import flet as ft
from ..widgets.post_card import PostCard
from ..widgets.nav_bar import create_nav_bar
from mock.posts import get_mock_posts
from mock.comments import get_mock_comments


def dashboard(page: ft.Page):
    page.title = "Página inicial - Scambo"
    page.bgcolor = "#f5f5f5"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

    # Get sample feed data from mock module (easy to swap for real API later)
    mock_posts = get_mock_posts()

    feed_cards = []
    for idx, mp in enumerate(mock_posts):
        avatar = ft.CircleAvatar(
            bgcolor=mp["avatar_bg"], content=ft.Text(mp["avatar_text"], color="white")
        )
        # Get comments for this post (using index as post_id)
        post_comments = get_mock_comments(idx)

        feed_cards.append(
            ft.Container(
                alignment=ft.alignment.center,
                content=PostCard(
                    author_name=mp["author_name"],
                    author_avatar=avatar,
                    post_title=mp["post_title"],
                    post_description=mp["post_description"],
                    post_date=mp["post_date"],
                    image_path=mp.get("image_path"),
                    tags=mp.get("tags"),
                    comments=post_comments,
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

    # Get reusable navigation bar
    nav = create_nav_bar(page, selected_index=0)

    # Main layout: expandable feed + bottom navigation (no top bar)
    page.add(
        ft.Column(
            [
                feed_list,
                nav,
            ],
            expand=True,
            spacing=0,
        )
    )
