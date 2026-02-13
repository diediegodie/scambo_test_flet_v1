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

import flet as ft
from run_app import main

if __name__ == "__main__":
    ft.run(main)
