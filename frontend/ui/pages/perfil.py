# When wire the backend:
# Replace mock.user.get_current_user() with an async API call
# Add JWT token handling in core/ for authenticated requests
# Define a UserSchema in schemas/user.py for validation

import flet as ft
from ..widgets.new_post_dialog import open_new_post_dialog
from ..widgets.nav_bar import create_nav_bar
from ..theme import AppTheme
from mock.user import get_current_user
from mock.posts import count_user_posts


def perfil(page: ft.Page, is_dark_mode: bool = False):
    """
    Professional user profile page with avatar, bio, stats, and actions.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """
    page.title = "Perfil - Scambo"
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )
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
                    color=AppTheme.TEXT_ON_COLORED_BG,
                    size=AppTheme.ICON_SIZE_XL,  # 40px
                    weight=AppTheme.FONT_WEIGHT_BOLD,
                ),
                radius=AppTheme.AVATAR_RADIUS_LARGE,
            ),
            ft.Text(
                user["name"],
                size=AppTheme.FONT_SIZE_TITLE,
                weight=AppTheme.FONT_WEIGHT_BOLD,
                color=(
                    AppTheme.DARK_TEXT_PRIMARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_PRIMARY
                ),
            ),
            ft.Text(
                user["email"],
                size=AppTheme.FONT_SIZE_BODY,
                color=(
                    AppTheme.DARK_TEXT_TERTIARY
                    if is_dark_mode
                    else AppTheme.LIGHT_TEXT_TERTIARY
                ),
            ),
            # Bio section
            ft.Container(
                content=ft.Text(
                    user["bio"],
                    size=AppTheme.FONT_SIZE_BODY,
                    color=(
                        AppTheme.DARK_TEXT_SECONDARY
                        if is_dark_mode
                        else AppTheme.LIGHT_TEXT_SECONDARY
                    ),
                    text_align=ft.TextAlign.CENTER,
                ),
                width=AppTheme.CARD_WIDTH_NARROW,
                padding=ft.padding.only(top=AppTheme.SPACING_SM),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=AppTheme.SPACING_SM,
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
                                    color=AppTheme.PRIMARY_GREEN,
                                    size=AppTheme.ICON_SIZE_LG,  # 24px
                                ),
                                ft.Text(
                                    str(user_posts_count),
                                    size=AppTheme.FONT_SIZE_TITLE,
                                    weight=AppTheme.FONT_WEIGHT_BOLD,
                                    color=(
                                        AppTheme.DARK_TEXT_PRIMARY
                                        if is_dark_mode
                                        else AppTheme.LIGHT_TEXT_PRIMARY
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=AppTheme.SPACING_SM,
                        ),
                        ft.Text(
                            "Publicações",
                            size=AppTheme.FONT_SIZE_CAPTION,
                            color=(
                                AppTheme.DARK_TEXT_TERTIARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_TERTIARY
                            ),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=AppTheme.SPACING_XS,  # 4px
                ),
                padding=AppTheme.SPACING_MD,
                border_radius=AppTheme.CARD_BORDER_RADIUS,
                bgcolor=(
                    AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE
                ),
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
                                    color=AppTheme.WARNING,
                                    size=AppTheme.ICON_SIZE_LG,  # 24px
                                ),
                                ft.Text(
                                    f"{user['reputation']:.1f}",
                                    size=AppTheme.FONT_SIZE_TITLE,
                                    weight=AppTheme.FONT_WEIGHT_BOLD,
                                    color=(
                                        AppTheme.DARK_TEXT_PRIMARY
                                        if is_dark_mode
                                        else AppTheme.LIGHT_TEXT_PRIMARY
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=AppTheme.SPACING_SM,
                        ),
                        ft.Text(
                            "Reputação",
                            size=AppTheme.FONT_SIZE_CAPTION,
                            color=(
                                AppTheme.DARK_TEXT_TERTIARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_TERTIARY
                            ),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=AppTheme.SPACING_XS,  # 4px
                ),
                padding=AppTheme.SPACING_MD,
                border_radius=AppTheme.CARD_BORDER_RADIUS,
                bgcolor=(
                    AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE
                ),
                expand=True,
            ),
        ],
        spacing=AppTheme.SPACING_MD,
        width=AppTheme.CARD_WIDTH_NARROW,
    )

    # Button for new publication (matching dashboard style)
    novo_button = AppTheme.get_elevated_button(
        "Nova publicação",
        on_click=lambda e: open_new_post_dialog(page, is_dark_mode),
        width=AppTheme.BUTTON_WIDTH_MEDIUM,
        height=AppTheme.BUTTON_HEIGHT,
    )

    # Main content card (centered like login/create account)
    content_card = ft.Card(
        elevation=AppTheme.CARD_ELEVATION,
        color=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
        content=ft.Container(
            content=ft.Column(
                [
                    profile_header,
                    AppTheme.get_divider(is_dark_mode),
                    stats_row,
                    novo_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=AppTheme.SPACING_LG,
            ),
            padding=AppTheme.SPACING_XL + 8,  # 40px
            width=AppTheme.CARD_WIDTH_PROFILE,
            border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
        ),
    )

    # Get reusable navigation bar
    nav = create_nav_bar(
        page, selected_index=2, is_dark_mode=is_dark_mode
    )  # Profile is selected

    # Main layout with centered content and bottom navigation (no top bar)
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
