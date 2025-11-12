"""Search page with search field and photo grid feed.

Displays a search bar at the top and a grid of post images below:
- Themed search TextField with icon
- GridView photo feed (Instagram Explore-style)
- Fully responsive layout (adaptive column count + flexible width)
- Lazy loading for images (viewport-based rendering)
- Image caching for smooth scrolling
- Tap photo to view full post (future feature)
- All styling uses theme.py constants for consistency

Backend migration:
- Replace get_mock_posts() with API call: GET /search/posts?q={query}
- Implement filters: category, location, date range
- Add infinite scroll with pagination
"""

import flet as ft
from ..widgets.nav_bar import create_nav_bar
from ..theme import AppTheme
from mock.posts import get_mock_posts


def search(page: ft.Page, is_dark_mode: bool = False):
    """
    Search page with photo grid feed.

    Parameters
    ----------
    page : ft.Page
        Flet page instance
    is_dark_mode : bool, optional
        Whether to use dark theme styling
    """
    page.title = "Buscar - Scambo"
    page.bgcolor = (
        AppTheme.DARK_BACKGROUND if is_dark_mode else AppTheme.LIGHT_BACKGROUND
    )
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

    # State management
    search_query = ""
    all_posts = get_mock_posts()
    photo_grid = None  # Will be initialized after calculating columns
    content_container = None  # Will be initialized after creation
    search_field = None  # Will be initialized after creation
    search_btn = None  # Left action button
    clear_btn = None  # Right clear button
    debounce_timer = None  # Timer for debouncing search input

    def get_window_width() -> int:
        """Safely get current window width as int with fallback."""
        try:
            w = page.window.width or page.width or 800
            return int(w)
        except Exception:
            return 800

    def get_responsive_columns(window_width: int | None = None):
        """
        Calculate grid columns based on window width.
        - Small screens (<600px): 2 columns
        - Tablets (600-900px): 3 columns
        - Desktop (>900px): 4 columns
        """
        ww = window_width if window_width is not None else get_window_width()
        if ww < 600:
            return 2
        elif ww < 900:
            return 3
        else:
            return 4

    def execute_search():
        """Execute the search action with current query."""
        nonlocal search_query
        # Future: Call API with search query
        # For now, just log the search action
        print(f"Executing search for: {search_query}")  # Debug
        # Future: Filter posts, call API, update grid, etc.

    # on_search_change and on_clear_click are defined later (after buttons are created)

    def on_search_click(e):
        """Trigger search when magnifying glass icon is clicked."""
        execute_search()

    def on_key_press(e):
        """Handle keyboard shortcuts."""
        nonlocal search_query, search_field
        if e.key == "Enter":
            execute_search()
        elif e.key == "Escape":
            on_clear_click(e)

    # External clear button will be created later and its disabled state updated dynamically

    # Define handlers before field/button creation so they can be referenced
    def on_search_change(e):
        """Handle search input changes with debouncing and clear button state."""
        nonlocal search_query, debounce_timer, search_field, clear_btn
        search_query = e.control.value.lower()

        # Enable or disable clear button based on current text
        if clear_btn is not None:
            clear_btn.disabled = not bool(search_query)
            clear_btn.update()

        # Cancel previous timer if exists
        if debounce_timer:
            debounce_timer.cancel()

        # Set new timer for debounced search (300ms delay)
        import threading

        debounce_timer = threading.Timer(0.3, execute_search)
        debounce_timer.start()

    def on_clear_click(e):
        """Clear the search field and disable clear button."""
        nonlocal search_query, search_field, clear_btn
        search_query = ""
        if search_field:
            search_field.value = ""
            search_field.update()
            search_field.focus()
        if clear_btn:
            clear_btn.disabled = True
            clear_btn.update()

    def on_photo_click(e):
        """Handle photo click - future: open post detail modal."""
        post_index = e.control.data
        post = all_posts[post_index]
        print(f"Clicked on post: {post['post_title']}")  # Debug
        # Future: Open post detail modal or navigate to post page
        snack = ft.SnackBar(
            content=ft.Text(f"Post: {post['post_title']} (em breve)"),
            bgcolor=AppTheme.INFO,
        )
        page.overlay.append(snack)
        snack.open = True
        page.update()

    # Search field with floating label (consistent with login page inputs)
    # Layout: [Search Button] [TextField (expand)] [Clear Button]
    search_field = AppTheme.get_input_field(
        label="Buscar",
        hint_text="Buscar publicações, tags, usuários...",
        is_dark_mode=is_dark_mode,
        expand=1,  # Fill remaining horizontal space inside Row
        on_change=on_search_change,
        on_submit=lambda e: execute_search(),  # Enter key support
        autofocus=False,
    )

    # Left search action button
    search_btn = ft.IconButton(
        icon=ft.Icons.SEARCH,
        icon_size=AppTheme.ICON_SIZE_LG,
        icon_color=AppTheme.PRIMARY_GREEN,
        tooltip="Buscar",
        on_click=on_search_click,
    )

    # Right clear action button (disabled when empty)
    clear_btn = ft.IconButton(
        icon=ft.Icons.CLEAR,
        icon_size=AppTheme.ICON_SIZE_LG,
        icon_color=(
            AppTheme.DARK_TEXT_SECONDARY if is_dark_mode else AppTheme.LIGHT_TEXT_SECONDARY
        ),
        tooltip="Limpar",
        disabled=True,  # Initially disabled until user types
        on_click=on_clear_click,
    )

    # (Handlers defined above)

    def build_photo_grid():
        """Build photo grid with responsive columns and lazy loading."""
        nonlocal photo_grid

        photo_items = []
        for idx, post in enumerate(all_posts):
            if post.get("image_path"):
                # Create image container with tap handler
                # Lazy loading: Images load when GridView renders them (Flet's default behavior)
                # Caching: Set gapless_playback=True for smooth re-rendering
                photo_items.append(
                    ft.Container(
                        content=ft.Image(
                            src=post["image_path"],
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(AppTheme.SPACING_XS),
                            gapless_playback=True,  # Enable image caching
                            error_content=ft.Icon(
                                ft.Icons.BROKEN_IMAGE,
                                size=AppTheme.ICON_SIZE_XL,
                                color=(
                                    AppTheme.DARK_TEXT_TERTIARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_TERTIARY
                                ),
                            ),
                        ),
                        bgcolor=(
                            AppTheme.DARK_SURFACE_VARIANT
                            if is_dark_mode
                            else AppTheme.LIGHT_SURFACE_VARIANT
                        ),
                        border_radius=ft.border_radius.all(AppTheme.SPACING_XS),
                        ink=True,
                        on_click=on_photo_click,
                        data=idx,  # Store post index for click handler
                        aspect_ratio=1.0,  # Maintain square aspect ratio
                    )
                )

        # Grid view for photos with responsive columns
        columns = get_responsive_columns()
        photo_grid = ft.GridView(
            controls=photo_items,
            runs_count=columns,  # Dynamic column count
            max_extent=150,  # Max width of each grid item
            spacing=AppTheme.SPACING_SM,
            run_spacing=AppTheme.SPACING_SM,
            expand=True,
            padding=0,
            child_aspect_ratio=1.0,  # Keep items square
        )
        return photo_grid

    def on_page_resize(e):
        """Handle window resize to update grid columns."""
        nonlocal photo_grid, content_container
        changed = False
        if photo_grid:
            ww = get_window_width()
            new_columns = get_responsive_columns(ww)
            if photo_grid.runs_count != new_columns:
                photo_grid.runs_count = new_columns
                changed = True
        if content_container:
            ww = get_window_width()
            new_width = AppTheme.get_responsive_container_width(ww)
            if content_container.width != new_width:
                content_container.width = new_width
                changed = True
        if changed:
            page.update()

    # Register resize handler
    page.on_resized = on_page_resize

    # Register keyboard handler for shortcuts (Esc to clear)
    page.on_keyboard_event = on_key_press

    # Build initial grid
    photo_grid = build_photo_grid()

    # Content container with discrete responsive width (breakpoints)
    # Uses padding for consistent spacing; remains centered by parent container
    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Container(height=AppTheme.SPACING_LG),
                # Page title
                ft.Text(
                    "Explorar",
                    size=AppTheme.FONT_SIZE_TITLE,
                    weight=AppTheme.FONT_WEIGHT_BOLD,
                    color=(
                        AppTheme.DARK_TEXT_PRIMARY
                        if is_dark_mode
                        else AppTheme.LIGHT_TEXT_PRIMARY
                    ),
                ),
                ft.Container(height=AppTheme.SPACING_MD),
                # Search bar: [search] [input] [clear]
                ft.Row(
                    controls=[
                        search_btn,
                        search_field,
                        clear_btn,
                    ],
                    spacing=AppTheme.SPACING_SM,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=AppTheme.SPACING_MD),
                AppTheme.get_divider(is_dark_mode),
                ft.Container(height=AppTheme.SPACING_SM),
                # Photo grid
                photo_grid,
            ],
            spacing=0,
        ),
        width=AppTheme.get_responsive_container_width(get_window_width()),
        padding=ft.padding.symmetric(horizontal=AppTheme.SPACING_MD),
        expand=True,
    )

    # Get navigation bar
    nav = create_nav_bar(page, selected_index=3, is_dark_mode=is_dark_mode)

    # Main layout with centered content
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=content_container,
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
    ft.app(target=search)
