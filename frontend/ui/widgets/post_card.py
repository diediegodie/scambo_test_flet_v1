"""Reusable PostCard widget for SCAMBO feed.

This component encapsulates visual representation of a user publication.
Use only from page-level modules (e.g., dashboard, profile feeds).
"""

from __future__ import annotations
import flet as ft
from typing import List


def PostCard(
    author_name: str,
    author_avatar: ft.CircleAvatar,
    post_title: str,
    post_description: str,
    post_date: str,
    image_path: str | None = None,
    tags: List[str] | None = None,
    comments: List[dict] | None = None,
    width: int | None = 450,
) -> ft.Card:
    """Return a styled post card.

    Parameters
    ----------
    author_name: Display name of the author.
    author_avatar: Pre-built CircleAvatar (allows caller to decide color/content).
    post_title: Short headline for the publication.
    post_description: Longer descriptive text (truncated at 200 chars if needed).
    post_date: Human-readable date string.
    image_path: Optional path to post image. Uses placeholder if provided.
    tags: Optional list of tag strings to display below description.
    comments: Optional list of comment dicts with keys: author_name, avatar_bg, avatar_text, comment_text.
    width: Card width in pixels (default 450).
    """

    # Helper function to truncate description
    def truncate_text(text: str, max_length: int = 200) -> str:
        """Truncate text to max_length and add ellipsis if needed."""
        if len(text) <= max_length:
            return text
        return text[:max_length].rsplit(" ", 1)[0] + "..."

    # Header (author + date)
    header = ft.Row(
        [
            author_avatar,
            ft.Column(
                [
                    ft.Text(
                        author_name, weight=ft.FontWeight.BOLD, size=16, color="#333333"
                    ),
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

    # Image placeholder (if path provided)
    image_container = None
    if image_path:
        image_container = ft.Container(
            content=ft.Image(
                src=image_path,
                width=width - 30 if width else 420,  # Account for card padding
                height=200,
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(8),
            ),
            margin=ft.margin.only(top=8, bottom=8),
        )

    # Title + description with truncation
    truncated_description = truncate_text(post_description, 200)
    body = ft.Column(
        [
            ft.Text(post_title, size=15, weight=ft.FontWeight.W_600, color="#333333"),
            ft.Text(truncated_description, size=13, color="#555555"),
        ],
        spacing=6,
    )

    # Tags row (if tags provided)
    tags_row = None
    if tags:
        tag_chips = [
            ft.Container(
                content=ft.Text(
                    tag,
                    size=11,
                    color="white",
                    weight=ft.FontWeight.W_500,
                ),
                bgcolor="#4CAF50",
                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                border_radius=ft.border_radius.all(12),
            )
            for tag in tags
        ]
        tags_row = ft.Row(
            controls=tag_chips,
            spacing=6,
            wrap=True,
        )

    # Actions row
    like_btn = ft.IconButton(
        icon=ft.Icons.FAVORITE_BORDER, tooltip="Curtir", icon_color="#4CAF50"
    )
    comment_btn = ft.IconButton(
        icon=ft.Icons.CHAT_BUBBLE_OUTLINE, tooltip="Comentar", icon_color="#4CAF50"
    )
    share_btn = ft.IconButton(
        icon=ft.Icons.SHARE, tooltip="Compartilhar", icon_color="#4CAF50"
    )

    actions = ft.Row(
        [like_btn, comment_btn, share_btn],
        spacing=4,
        alignment=ft.MainAxisAlignment.START,
    )

    # Comments section (if comments provided)
    comments_section = None
    if comments:
        # Limit to first 3 comments
        displayed_comments = comments[:3]
        comment_widgets = []

        for comment in displayed_comments:
            comment_avatar = ft.CircleAvatar(
                bgcolor=comment.get("avatar_bg", "#9E9E9E"),
                content=ft.Text(
                    comment.get("avatar_text", "?"), color="white", size=12
                ),
                radius=16,
            )

            comment_widget = ft.Row(
                [
                    comment_avatar,
                    ft.Column(
                        [
                            ft.Text(
                                comment.get("author_name", "Anônimo"),
                                weight=ft.FontWeight.BOLD,
                                size=13,
                                color="#333333",
                            ),
                            ft.Text(
                                comment.get("comment_text", ""),
                                size=12,
                                color="#555555",
                            ),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
            comment_widgets.append(comment_widget)

        # Add "View more" button if there are more than 3 comments
        if len(comments) > 3:
            view_more_btn = ft.TextButton(
                text=f"Ver mais {len(comments) - 3} comentário(s)",
                style=ft.ButtonStyle(color="#4CAF50"),
            )
            comment_widgets.append(
                ft.Container(
                    content=view_more_btn,
                    padding=ft.padding.only(left=40, top=4),
                )
            )

        comments_section = ft.Column(
            controls=comment_widgets,
            spacing=8,
        )

    # Build card content with conditional elements
    card_elements = []
    card_elements.append(header)

    if image_container:
        card_elements.append(image_container)

    card_elements.append(body)

    if tags_row:
        card_elements.append(tags_row)

    card_elements.append(ft.Divider(height=8, color="#e0e0e0"))
    card_elements.append(actions)

    if comments_section:
        card_elements.append(ft.Divider(height=8, color="#e0e0e0"))
        card_elements.append(comments_section)

    return ft.Card(
        elevation=3,
        width=width,
        content=ft.Container(
            padding=15,
            content=ft.Column(
                card_elements,
                spacing=12,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),
    )
