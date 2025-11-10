"""Reusable PostCard widget for SCAMBO feed.

This component encapsulates visual representation of a user publication.
Use only from page-level modules (e.g., dashboard, profile feeds).
"""
from __future__ import annotations
import flet as ft


def PostCard(
    author_name: str,
    author_avatar: ft.CircleAvatar,
    post_title: str,
    post_description: str,
    post_date: str,
    width: int | None = 450,
) -> ft.Card:
    """Return a styled post card.

    Parameters
    ----------
    author_name: Display name of the author.
    author_avatar: Pre-built CircleAvatar (allows caller to decide color/content).
    post_title: Short headline for the publication.
    post_description: Longer descriptive text.
    post_date: Human-readable date string.
    """
    # Header (author + date)
    header = ft.Row(
        [
            author_avatar,
            ft.Column(
                [
                    ft.Text(author_name, weight=ft.FontWeight.BOLD, size=16, color="#333333"),
                    ft.Text(post_date, size=11, color="#777777"),
                ],
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=12,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Title + description
    body = ft.Column(
        [
            ft.Text(post_title, size=15, weight=ft.FontWeight.W_600, color="#333333"),
            ft.Text(post_description, size=13, color="#555555"),
        ],
        spacing=6,
    )

    # Actions row
    like_btn = ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, tooltip="Curtir", icon_color="#4CAF50")
    comment_btn = ft.IconButton(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, tooltip="Comentar", icon_color="#4CAF50")
    share_btn = ft.IconButton(icon=ft.Icons.SHARE, tooltip="Compartilhar", icon_color="#4CAF50")

    actions = ft.Row(
        [like_btn, comment_btn, share_btn],
        spacing=4,
        alignment=ft.MainAxisAlignment.START,
    )

    return ft.Card(
        elevation=3,
        width=width,
        content=ft.Container(
            padding=15,
            content=ft.Column(
                [header, body, ft.Divider(height=8, color="#e0e0e0"), actions],
                spacing=12,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),
    )
