"""
SCAMBO App - Main Entry Point (Alias)

This file is an alias to run_app.py for compatibility with Flet CLI.
When using 'flet run --android' or 'flet run --ios', Flet looks for main.py by default.

Usage:
    flet run --android
    flet run --ios
    
Or directly:
    python3 main.py
"""

from run_app import main
import flet as ft

if __name__ == "__main__":
    ft.app(target=main)
