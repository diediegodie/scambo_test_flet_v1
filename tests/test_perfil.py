"""
Test script to verify navigation between dashboard and profile pages.
This script launches the profile page directly to test the navigation.
"""
import flet as ft
from frontend.ui.pages.perfil import perfil


def main(page: ft.Page):
    """Launch profile page for testing."""
    perfil(page)


if __name__ == "__main__":
    ft.app(target=main)
