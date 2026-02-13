"""Reusable PostCard widget for SCAMBO feed.

This component encapsulates visual representation of a user publication.
Use only from page-level modules (e.g., dashboard, profile feeds).
"""

from __future__ import annotations
import flet as ft
from typing import List
from ..theme import AppTheme

def PostCard(
    author_name: str,
    author_avatar: ft.CircleAvatar,
    post_title: str,
    post_description: str,
    post_date: str,
    image_path: str | None = None,
    tags: List[str] | None = None,
    comments: List[dict] | None = None,
    width: int | None = None,
    is_dark_mode: bool = False,
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
    width: Card width in pixels (default CARD_WIDTH_STANDARD from theme).
    is_dark_mode: Whether to apply dark theme styling.
    """

    # Use theme default width if not specified
    card_width = width or AppTheme.CARD_WIDTH_STANDARD

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
                        author_name,
                        weight=AppTheme.FONT_WEIGHT_BOLD,
                        size=AppTheme.FONT_SIZE_BODY,
                        color=(
                            AppTheme.DARK_TEXT_PRIMARY
                            if is_dark_mode
                            else AppTheme.LIGHT_TEXT_PRIMARY
                        ),
                    ),
                    ft.Text(
                        post_date,
                        size=AppTheme.FONT_SIZE_SMALL,
                        color=(
                            AppTheme.DARK_TEXT_TERTIARY
                            if is_dark_mode
                            else AppTheme.LIGHT_TEXT_TERTIARY
                        ),
                    ),
                ],
                spacing=AppTheme.SPACING_XXS,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=AppTheme.SPACING_MD,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Image placeholder (if path provided)
    image_container = None
    if image_path:
        image_container = ft.Container(
            content=ft.Image(
                src=image_path,
                width=card_width - 30,  # Account for card padding
                height=AppTheme.POST_IMAGE_HEIGHT,
                fit=ft.BoxFit.COVER,
                border_radius=ft.border_radius.all(AppTheme.SPACING_SM),
            ),
            margin=ft.margin.only(top=AppTheme.SPACING_SM, bottom=AppTheme.SPACING_SM),
        )

    # Title + description with truncation
    truncated_description = truncate_text(post_description, 200)
    body = ft.Column(
        [
            ft.Text(
                post_title,
                size=AppTheme.FONT_SIZE_SUBTITLE,
                weight=AppTheme.FONT_WEIGHT_MEDIUM,
                color=(
                    AppTheme.DARK_TEXT_PRIMARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_PRIMARY
                ),
            ),
            ft.Text(
                truncated_description,
                size=AppTheme.FONT_SIZE_BODY,
                color=(
                    AppTheme.DARK_TEXT_SECONDARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_SECONDARY
                ),
            ),
        ],
        spacing=AppTheme.SPACING_SM,
    )

    # Tags row (if tags provided)
    tags_row = None
    if tags:
        tag_chips = [
            ft.Container(
                content=ft.Text(
                    tag,
                    size=AppTheme.FONT_SIZE_SMALL,
                    color=AppTheme.TEXT_ON_COLORED_BG,
                    weight=AppTheme.FONT_WEIGHT_MEDIUM,
                ),
                bgcolor=AppTheme.PRIMARY_GREEN,
                padding=ft.padding.symmetric(
                    horizontal=AppTheme.TAG_PADDING_HORIZONTAL,
                    vertical=AppTheme.TAG_PADDING_VERTICAL,
                ),
                border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
            )
            for tag in tags
        ]
        tags_row = ft.Row(
            controls=tag_chips,  # type: ignore
            spacing=AppTheme.SPACING_SM,
            wrap=True,
        )

    # Actions row
    like_btn = ft.IconButton(
        icon=ft.Icons.FAVORITE_BORDER,
        tooltip="Curtir",
        icon_color=AppTheme.PRIMARY_GREEN,
    )
    comment_btn = ft.IconButton(
        icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
        tooltip="Comentar",
        icon_color=AppTheme.PRIMARY_GREEN,
    )
    share_btn = ft.IconButton(
        icon=ft.Icons.SHARE, tooltip="Compartilhar", icon_color=AppTheme.PRIMARY_GREEN
    )

    actions = ft.Row(
        [like_btn, comment_btn, share_btn],
        spacing=AppTheme.SPACING_XS,
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
                bgcolor=comment.get("avatar_bg", AppTheme.DEFAULT_AVATAR_BG),
                content=ft.Text(
                    comment.get("avatar_text", "?"),
                    color=AppTheme.TEXT_ON_COLORED_BG,
                    size=AppTheme.FONT_SIZE_CAPTION,
                ),
                radius=AppTheme.AVATAR_RADIUS_SMALL,
            )

            comment_widget = ft.Row(
                [
                    comment_avatar,
                    ft.Column(
                        [
                            ft.Text(
                                comment.get("author_name", "Anônimo"),
                                weight=AppTheme.FONT_WEIGHT_BOLD,
                                size=AppTheme.FONT_SIZE_BODY,
                                color=(
                                    AppTheme.DARK_TEXT_PRIMARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_PRIMARY
                                ),
                            ),
                            ft.Text(
                                comment.get("comment_text", ""),
                                size=AppTheme.FONT_SIZE_CAPTION,
                                color=(
                                    AppTheme.DARK_TEXT_SECONDARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_SECONDARY
                                ),
                            ),
                        ],
                        spacing=AppTheme.SPACING_XXS,
                        expand=True,
                    ),
                ],
                spacing=AppTheme.SPACING_SM,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
            comment_widgets.append(comment_widget)

        # Add "View more" button if there are more than 3 comments
        if len(comments) > 3:
            view_more_btn = ft.TextButton(
                content=ft.Text(
                    f"Ver mais {len(comments) - 3} comentário(s)",
                    color=AppTheme.PRIMARY_GREEN,
                ),
            )
            comment_widgets.append(
                ft.Container(
                    content=view_more_btn,
                    padding=ft.padding.only(
                        left=AppTheme.COMMENT_INDENT, top=AppTheme.SPACING_XS
                    ),
                )
            )

        comments_section = ft.Column(
            controls=comment_widgets,
            spacing=AppTheme.SPACING_SM,
        )

    # Build card content with conditional elements
    card_elements = []
    card_elements.append(header)

    if image_container:
        card_elements.append(image_container)

    card_elements.append(body)

    if tags_row:
        card_elements.append(tags_row)

    card_elements.append(
        ft.Divider(
            height=AppTheme.DIVIDER_HEIGHT,
            color=AppTheme.DARK_BORDER if is_dark_mode else AppTheme.LIGHT_BORDER,
        )
    )
    card_elements.append(actions)

    if comments_section:
        card_elements.append(
            ft.Divider(
                height=AppTheme.DIVIDER_HEIGHT,
                color=AppTheme.DARK_BORDER if is_dark_mode else AppTheme.LIGHT_BORDER,
            )
        )
        card_elements.append(comments_section)

    return ft.Card(
        elevation=AppTheme.CARD_ELEVATION,
        width=card_width,
        content=ft.Container(
            padding=AppTheme.SPACING_MD,
            bgcolor=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
            content=ft.Column(
                card_elements,
                spacing=AppTheme.SPACING_MD,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
        ),
    )
