"""
SCAMBO App - Main Entry Point

Run this file to launch the application.
The app starts at the landing page (index.py) where you can navigate to login or create account.

Usage:
    python3 run_app.py
"""

import flet as ft
from frontend.ui.pages.index import index
from frontend.ui.theme import get_light_theme, get_dark_theme


def main(page: ft.Page):
    """Launch the SCAMBO app starting from the landing page."""
    # Get theme preference from client storage, default to light mode
    is_dark_mode = page.client_storage.get("is_dark_mode")
    if is_dark_mode is None:
        is_dark_mode = False  # Default to light mode
        page.client_storage.set("is_dark_mode", is_dark_mode)

    # Set theme based on preference
    page.theme = get_dark_theme() if is_dark_mode else get_light_theme()

    # Launch the app
    index(page, is_dark_mode)


if __name__ == "__main__":
    ft.app(target=main)
