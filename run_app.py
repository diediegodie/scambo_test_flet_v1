"""
SCAMBO App - Main Entry Point

Run this file to launch the application.
The app starts at the landing page (index.py) where you can navigate to login or create account.

Usage:
    python3 run_app.py
"""

import flet as ft
from frontend.ui.pages.index import index


def main(page: ft.Page):
    """Launch the SCAMBO app starting from the landing page."""
    index(page)


if __name__ == "__main__":
    ft.app(target=main)
