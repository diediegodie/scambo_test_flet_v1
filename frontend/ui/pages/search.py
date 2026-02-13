"""Search page with search field and photo grid feed.

Displays a search bar at the top and a grid of post images below:
- Themed search TextField with icon
- GridView photo feed (Instagram Explore-style)
- Fully responsive layout (adaptive column count + flexible width)
- Lazy loading for images (viewport-based rendering)
- Image caching for smooth scrolling
- Tap photo to open post detail dialog modal
- All styling uses theme.py constants for consistency

Backend migration:
- Replace get_mock_posts() with API call: GET /search/posts?q={query}
- Implement filters: category, location, date range
- Add infinite scroll with pagination
"""

import asyncio
import flet as ft
from ..widgets.nav_bar import create_nav_bar
from ..widgets.post_detail_dialog import open_post_detail_dialog
from ..theme import AppTheme
from mock.posts import get_mock_posts, get_unique_categories, get_paginated_posts


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
    _all_posts = (
        get_mock_posts()
    )  # Keep for backward compatibility (not used with pagination)
    filtered_posts = (
        []
    )  # Posts after filtering by search query (cumulative with pagination)
    is_loading = False  # Loading state for async operations
    photo_grid = None  # Will be initialized after calculating columns
    content_container = None  # Will be initialized after creation
    search_field = None  # Will be initialized after creation
    search_btn = None  # Left action button
    clear_btn = None  # Right clear button
    debounce_timer = None  # Timer for debouncing search input
    selected_photo_index = (
        -1
    )  # Current focused photo index for keyboard navigation (-1 = none)
    photo_containers = []  # List of photo container references for keyboard navigation

    # Filter and pagination state
    category_filter = None  # Currently selected category (None = "Todos")
    current_page = 1  # Current page number
    page_size = 6  # Posts per page
    has_more = True  # Whether there are more posts to load
    total_posts = 0  # Total number of posts matching current filters
    is_loading_more = False  # Loading state for pagination

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

    async def execute_search():
        """Execute the search action with current query and filters asynchronously."""
        nonlocal search_query, filtered_posts, is_loading, photo_grid, current_page, has_more, total_posts, photo_containers, selected_photo_index

        # Reset pagination when search/filter changes
        current_page = 1
        filtered_posts = []
        photo_containers = []
        selected_photo_index = -1

        # Set loading state
        is_loading = True
        if photo_grid:
            photo_grid = build_photo_grid()
            update_grid_in_content()

        # Simulate API call delay (remove in production)
        await asyncio.sleep(0.8)

        # Get paginated posts with search query and category filter
        result = get_paginated_posts(
            page=current_page,
            page_size=page_size,
            search_query=search_query.strip() if search_query.strip() else None,
            category_filter=category_filter,
        )

        # Update state from pagination result
        filtered_posts = result["posts"]
        has_more = result["has_more"]
        total_posts = result["total"]

        # Clear loading state
        is_loading = False
        if photo_grid:
            photo_grid = build_photo_grid()
            update_grid_in_content()

    # on_search_change and on_clear_click are defined later (after buttons are created)

    def on_search_click(_e):
        """Trigger search when magnifying glass icon is clicked."""
        page.run_task(execute_search)

    def on_key_press(e):
        """Handle keyboard shortcuts and grid navigation."""
        nonlocal search_query, search_field, selected_photo_index, filtered_posts

        # Search field shortcuts (when not navigating grid)
        if selected_photo_index == -1:
            if e.key == "Enter":
                page.run_task(execute_search)
            elif e.key == "Escape":
                on_clear_click(e)
            elif e.key == "Tab" and not is_loading and filtered_posts:
                # Tab key: focus first photo in grid
                selected_photo_index = 0
                update_photo_focus()
                return
        else:
            # Grid navigation (when a photo is focused)
            columns = get_responsive_columns()
            total_photos = len(filtered_posts)

            if e.key == "Arrow Right":
                # Move right
                if selected_photo_index < total_photos - 1:
                    selected_photo_index += 1
                    update_photo_focus()
            elif e.key == "Arrow Left":
                # Move left
                if selected_photo_index > 0:
                    selected_photo_index -= 1
                    update_photo_focus()
            elif e.key == "Arrow Down":
                # Move down (next row)
                new_index = selected_photo_index + columns
                if new_index < total_photos:
                    selected_photo_index = new_index
                    update_photo_focus()
            elif e.key == "Arrow Up":
                # Move up (previous row)
                new_index = selected_photo_index - columns
                if new_index >= 0:
                    selected_photo_index = new_index
                    update_photo_focus()
            elif e.key == "Enter" or e.key == " ":
                # Enter or Space: open selected photo detail
                if 0 <= selected_photo_index < total_photos:
                    post = filtered_posts[selected_photo_index]
                    open_post_detail_dialog(
                        page=page,
                        post_data=post,
                        is_dark_mode=is_dark_mode,
                    )
            elif e.key == "Escape":
                # Escape: exit grid navigation
                selected_photo_index = -1
                update_photo_focus()

    # External clear button will be created later and its disabled state updated dynamically

    # Define handlers before field/button creation so they can be referenced
    def on_search_change(search_e):
        """Handle search input changes with debouncing and clear button state."""
        nonlocal search_query, debounce_timer, search_field, clear_btn
        search_query = search_e.control.value.lower()

        # Enable or disable clear button based on current text
        if clear_btn is not None:
            clear_btn.disabled = not bool(search_query)
            clear_btn.update()

        # Cancel previous timer if exists
        if debounce_timer:
            debounce_timer.cancel()

        # Set new timer for debounced search (300ms delay)
        import threading

        def trigger_search():
            """Schedule async search task on Flet's event loop."""
            page.run_task(execute_search)

        debounce_timer = threading.Timer(0.3, trigger_search)
        debounce_timer.start()

    def on_clear_click(_e):
        """Clear the search field and disable clear button."""
        nonlocal search_query, search_field, clear_btn
        search_query = ""
        if search_field:
            search_field.value = ""
            search_field.update()
        if clear_btn:
            clear_btn.disabled = True
            clear_btn.update()

    def on_photo_click(photo_e):
        """Handle photo click - open post detail modal."""
        post_index = photo_e.control.data
        post = filtered_posts[post_index]

        # Open post detail dialog with full post information
        open_post_detail_dialog(
            page=page,
            post_data=post,
            is_dark_mode=is_dark_mode,
        )

    def on_photo_hover(e):
        """Handle hover state changes for photo containers with scale and shadow effects."""
        container = e.control
        idx = container.data

        # Don't apply hover effect if this photo is keyboard-focused
        if idx == selected_photo_index:
            return

        if e.data == "true":  # Mouse entered
            container.scale = AppTheme.PHOTO_HOVER_SCALE
            container.shadow = ft.BoxShadow(
                spread_radius=AppTheme.PHOTO_HOVER_SHADOW_SPREAD,
                blur_radius=AppTheme.PHOTO_HOVER_SHADOW_BLUR,
                color=(
                    AppTheme.PHOTO_HOVER_SHADOW_COLOR_DARK
                    if is_dark_mode
                    else AppTheme.PHOTO_HOVER_SHADOW_COLOR_LIGHT
                ),
                offset=ft.Offset(0, AppTheme.PHOTO_HOVER_SHADOW_OFFSET_Y),
            )
        else:  # Mouse left
            container.scale = 1.0
            container.shadow = ft.BoxShadow(
                spread_radius=0,
                blur_radius=0,
                color=AppTheme.PHOTO_DEFAULT_SHADOW_COLOR,
                offset=ft.Offset(0, 0),
            )
        container.update()

    def update_photo_focus():
        """Update visual focus indicator for keyboard navigation."""
        nonlocal photo_containers, selected_photo_index

        # Reset all containers to default state
        for i, container in enumerate(photo_containers):
            if i == selected_photo_index:
                # Apply focus style (same as hover but with green border)
                container.scale = AppTheme.PHOTO_HOVER_SCALE
                container.shadow = ft.BoxShadow(
                    spread_radius=AppTheme.PHOTO_HOVER_SHADOW_SPREAD + 1,
                    blur_radius=AppTheme.PHOTO_HOVER_SHADOW_BLUR + 2,
                    color=AppTheme.PRIMARY_GREEN + "60",  # Green with 60% opacity
                    offset=ft.Offset(0, AppTheme.PHOTO_HOVER_SHADOW_OFFSET_Y),
                )
                container.border = ft.border.all(
                    AppTheme.BORDER_WIDTH_STANDARD, AppTheme.PRIMARY_GREEN
                )
            else:
                # Reset to default
                container.scale = 1.0
                container.shadow = ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=0,
                    color=AppTheme.PHOTO_DEFAULT_SHADOW_COLOR,
                    offset=ft.Offset(0, 0),
                )
                container.border = None
            container.update()

        page.update()

    # Search field with floating label (consistent with login page inputs)
    # Layout: [Search Button] [TextField (expand)] [Clear Button]
    search_field = AppTheme.get_input_field(
        label="Buscar",
        hint_text="Buscar publicações, tags, usuários...",
        is_dark_mode=is_dark_mode,
        expand=1,  # Fill remaining horizontal space inside Row
        on_change=on_search_change,
        on_submit=lambda _e: page.run_task(execute_search),  # Enter key support
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
            AppTheme.DARK_TEXT_SECONDARY
            if is_dark_mode
            else AppTheme.LIGHT_TEXT_SECONDARY
        ),
        tooltip="Limpar",
        disabled=True,  # Initially disabled until user types
        on_click=on_clear_click,
    )

    # Filter chips handlers
    def on_filter_click(category: str | None):
        """Handle filter chip click to filter posts by category.

        Parameters
        ----------
        category : str | None
            Category to filter by. None means "Todos" (all categories).
        """
        nonlocal category_filter, current_page, filtered_posts, photo_containers, selected_photo_index

        # Update selected filter
        category_filter = category

        # Reset pagination
        current_page = 1
        filtered_posts = []
        photo_containers = []
        selected_photo_index = -1

        # Rebuild filter chips to update visual state
        filter_chips_row.controls = build_filter_chips()
        filter_chips_row.update()

        # Execute search with new filter
        page.run_task(execute_search)

    def build_filter_chips():
        """Build filter chips UI with "Todos" + category chips.

        Returns
        -------
        list[ft.Control]
            List of chip controls.
        """
        categories = get_unique_categories()
        chips = []

        # "Todos" chip (always first)
        is_selected = category_filter is None
        chips.append(
            ft.Container(
                content=ft.Text(
                    "Todos",
                    size=AppTheme.FONT_SIZE_SMALL,
                    weight=ft.FontWeight.W_500 if is_selected else ft.FontWeight.W_400,
                    color=(
                        "#FFFFFF"
                        if is_selected
                        else (
                            AppTheme.DARK_TEXT_PRIMARY
                            if is_dark_mode
                            else AppTheme.LIGHT_TEXT_PRIMARY
                        )
                    ),
                ),
                padding=ft.padding.symmetric(
                    horizontal=AppTheme.TAG_PADDING_HORIZONTAL,
                    vertical=AppTheme.TAG_PADDING_VERTICAL,
                ),
                border_radius=ft.border_radius.all(100),
                bgcolor=(
                    AppTheme.PRIMARY_GREEN
                    if is_selected
                    else (
                        AppTheme.DARK_SURFACE_VARIANT
                        if is_dark_mode
                        else AppTheme.LIGHT_SURFACE_VARIANT
                    )
                ),
                border=ft.border.all(
                    2,
                    AppTheme.PRIMARY_GREEN if is_selected else "transparent",
                ),
                on_click=lambda e: on_filter_click(None),
                ink=True,
            )
        )

        # Category chips
        for category in categories:
            is_selected = category_filter == category
            chips.append(
                ft.Container(
                    ft.Text(
                        category.capitalize(),
                        size=AppTheme.FONT_SIZE_SMALL,
                        weight=(
                            ft.FontWeight.W_500 if is_selected else ft.FontWeight.W_400
                        ),
                        color=(
                            "#FFFFFF"
                            if is_selected
                            else (
                                AppTheme.DARK_TEXT_PRIMARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_PRIMARY
                            )
                        ),
                    ),
                    padding=ft.padding.symmetric(
                        horizontal=AppTheme.TAG_PADDING_HORIZONTAL,
                        vertical=AppTheme.TAG_PADDING_VERTICAL,
                    ),
                    border_radius=ft.border_radius.all(100),
                    bgcolor=(
                        AppTheme.PRIMARY_GREEN
                        if is_selected
                        else (
                            AppTheme.DARK_SURFACE_VARIANT
                            if is_dark_mode
                            else AppTheme.LIGHT_SURFACE_VARIANT
                        )
                    ),
                    border=ft.border.all(
                        2,
                        AppTheme.PRIMARY_GREEN if is_selected else "transparent",
                    ),
                    on_click=lambda e, cat=category: on_filter_click(cat),
                    ink=True,
                )
            )

        return chips

    # Initialize filter chips row (will be populated after content_container creation)
    filter_chips_row = ft.Row(
        controls=[],
        spacing=AppTheme.SPACING_SM,
        scroll=ft.ScrollMode.AUTO,  # Horizontal scroll if categories overflow
        alignment=ft.MainAxisAlignment.START,
    )

    # Load more handler for pagination
    async def load_more_posts():
        """Load next page of posts and append to current results."""
        nonlocal current_page, filtered_posts, has_more, is_loading_more, photo_grid, total_posts

        if is_loading_more or not has_more:
            return

        # Set loading state
        is_loading_more = True
        photo_grid = build_photo_grid()
        update_grid_in_content()

        # Simulate API delay
        await asyncio.sleep(0.8)

        # Load next page
        current_page += 1
        result = get_paginated_posts(
            page=current_page,
            page_size=page_size,
            search_query=search_query.strip() if search_query.strip() else None,
            category_filter=category_filter,
        )

        # Append new posts to existing results
        filtered_posts.extend(result["posts"])
        has_more = result["has_more"]
        total_posts = result["total"]

        is_loading_more = False
        photo_grid = build_photo_grid()
        update_grid_in_content()

    # (Handlers defined above)

    def build_photo_grid():
        """Build photo grid with responsive columns, loading, and empty states."""
        nonlocal photo_grid

        # Loading state: show centered spinner
        if is_loading:
            return ft.Container(
                content=ft.Column(
                    [
                        ft.ProgressRing(
                            width=AppTheme.ICON_SIZE_XL * 2,
                            height=AppTheme.ICON_SIZE_XL * 2,
                            stroke_width=4,
                            color=AppTheme.PRIMARY_GREEN,
                        ),
                        ft.Container(height=AppTheme.SPACING_MD),
                        ft.Text(
                            "Buscando publicações...",
                            size=AppTheme.FONT_SIZE_BODY,
                            color=(
                                AppTheme.DARK_TEXT_SECONDARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_SECONDARY
                            ),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                expand=True,
                alignment=ft.Alignment.CENTER,
            )

        # Empty state: no results found
        if not filtered_posts:
            return ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(
                            ft.Icons.IMAGE_SEARCH,
                            size=AppTheme.ICON_SIZE_XL * 2,
                            color=(
                                AppTheme.DARK_TEXT_TERTIARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_TERTIARY
                            ),
                        ),
                        ft.Container(height=AppTheme.SPACING_MD),
                        ft.Text(
                            "Nenhuma publicação encontrada",
                            size=AppTheme.FONT_SIZE_SUBTITLE,
                            weight=AppTheme.FONT_WEIGHT_MEDIUM,
                            color=(
                                AppTheme.DARK_TEXT_PRIMARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_PRIMARY
                            ),
                        ),
                        ft.Container(height=AppTheme.SPACING_XS),
                        ft.Text(
                            "Tente outra busca ou explore sem filtros",
                            size=AppTheme.FONT_SIZE_BODY,
                            color=(
                                AppTheme.DARK_TEXT_SECONDARY
                                if is_dark_mode
                                else AppTheme.LIGHT_TEXT_SECONDARY
                            ),
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                expand=True,
                alignment=ft.Alignment.CENTER,
            )

        # Content state: build grid with filtered posts
        photo_items = []
        photo_containers.clear()  # Reset containers list for keyboard navigation

        for idx, post in enumerate(filtered_posts):
            if post.get("image_path"):
                # Create accessible description for screen readers
                post_title = post.get("post_title", "Publicação")
                author_name = post.get("author_name", "Usuário")
                alt_text = f"{post_title} por {author_name}"

                # Create image container with tap handler
                # Lazy loading: Images load when GridView renders them (Flet's default behavior)
                # Caching: Set gapless_playback=True for smooth re-rendering
                container = ft.Container(
                    content=ft.Image(
                        src=post["image_path"],
                        fit=ft.BoxFit.COVER,
                        border_radius=ft.border_radius.all(AppTheme.SPACING_XS),
                        gapless_playback=True,  # Enable image caching
                        tooltip=alt_text,  # Hover tooltip for accessibility
                        semantics_label=alt_text,  # Screen reader description
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
                    on_hover=on_photo_hover,  # Enable hover effects
                    data=idx,  # Store post index for click and navigation
                    aspect_ratio=1.0,  # Maintain square aspect ratio
                    animate_scale=ft.Animation(
                        AppTheme.ANIMATION_DURATION_FAST,
                        ft.AnimationCurve.EASE_OUT,
                    ),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=0,
                        color=AppTheme.PHOTO_DEFAULT_SHADOW_COLOR,
                        offset=ft.Offset(0, 0),
                    ),
                )

                photo_items.append(container)
                photo_containers.append(
                    container
                )  # Store reference for keyboard navigation

        # Grid view for photos with responsive columns
        columns = get_responsive_columns()
        grid_view = ft.GridView(
            controls=photo_items,
            runs_count=columns,  # Dynamic column count
            max_extent=150,  # Max width of each grid item
            spacing=AppTheme.SPACING_SM,
            run_spacing=AppTheme.SPACING_SM,
            expand=True,
            padding=0,
            child_aspect_ratio=1.0,  # Keep items square
        )

        # Build Load More button (only if there are more posts)
        load_more_controls = []
        if has_more and filtered_posts:
            load_more_btn = ft.Container(
                content=ft.Row(
                    [
                        ft.ProgressRing(
                            width=AppTheme.ICON_SIZE_MD,
                            height=AppTheme.ICON_SIZE_MD,
                            stroke_width=2,
                            color=AppTheme.PRIMARY_GREEN,
                            visible=is_loading_more,
                        ),
                        ft.Text(
                            "Carregando..." if is_loading_more else "Carregar mais",
                            size=AppTheme.FONT_SIZE_BODY,
                            weight=AppTheme.FONT_WEIGHT_MEDIUM,
                            color=(
                                AppTheme.PRIMARY_GREEN
                                if not is_loading_more
                                else (
                                    AppTheme.DARK_TEXT_SECONDARY
                                    if is_dark_mode
                                    else AppTheme.LIGHT_TEXT_SECONDARY
                                )
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=AppTheme.SPACING_SM,
                ),
                padding=AppTheme.SPACING_MD,
                border_radius=ft.border_radius.all(AppTheme.CARD_BORDER_RADIUS),
                border=ft.border.all(1, AppTheme.PRIMARY_GREEN),
                bgcolor="transparent",
                ink=True,
                on_click=lambda _e: (page.run_task(load_more_posts) if not is_loading_more else None),  # type: ignore
            )
            load_more_controls = [
                ft.Container(height=AppTheme.SPACING_MD),
                ft.Container(
                    content=load_more_btn,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(height=AppTheme.SPACING_MD),
            ]

        # Wrap grid + load more button in a column
        all_controls: list[ft.Control] = [grid_view] + load_more_controls  # type: ignore
        photo_grid = ft.Column(
            controls=all_controls,
            spacing=0,
            expand=True,
        )
        return photo_grid

    def update_grid_in_content():
        """Update the photo grid in the content container."""
        nonlocal content_container, photo_grid
        if content_container and content_container.content and photo_grid:
            # Find the grid in the column and replace it
            column = content_container.content
            if isinstance(column, ft.Column) and len(column.controls) > 0:
                # Grid is the last item in the column
                column.controls[-1] = photo_grid
                page.update()

    def on_page_resize(_e):
        """Handle window resize to update grid columns."""
        nonlocal photo_grid, content_container
        changed = False
        # photo_grid is now a Column containing GridView + Load More button
        if photo_grid and isinstance(photo_grid, ft.Column):
            # Get the GridView (first child)
            if len(photo_grid.controls) > 0 and isinstance(
                photo_grid.controls[0], ft.GridView
            ):
                grid_view = photo_grid.controls[0]
                ww = get_window_width()
                new_columns = get_responsive_columns(ww)
                if grid_view.runs_count != new_columns:
                    grid_view.runs_count = new_columns
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
    page.on_resize = on_page_resize

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
                ft.Container(height=AppTheme.SPACING_MD),
                # Filter chips row
                filter_chips_row,
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

    # Populate filter chips after content_container creation
    filter_chips_row.controls = build_filter_chips()

    # Get navigation bar
    nav = create_nav_bar(page, selected_index=3, is_dark_mode=is_dark_mode)

    # Main layout with centered content
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=content_container,
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                ),
                nav,
            ],
            expand=True,
            spacing=0,
        )
    )

    # Load initial data
    page.run_task(execute_search)


if __name__ == "__main__":
    ft.app(target=search)
