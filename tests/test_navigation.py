"""
Quick test to verify dashboard navigation and layout.
Run this to test the Inicio button navigation in the dashboard.
"""

import flet as ft
from frontend.ui.pages.dashboard import dashboard


def main(page: ft.Page):
    """Launch directly to dashboard for testing."""
    dashboard(page)


if __name__ == "__main__":
    ft.app(target=main)
