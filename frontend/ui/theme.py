"""
Central theme definitions for the Scambo app.
Provides dark and light themes with consistent colors, typography, and component styles.

Dark theme: GitHub-inspired dark mode with subtle contrasts
Light theme: Burnt white background with soft grays for professional appearance
"""

import flet as ft


class AppTheme:
    """Centralized theme definitions for consistent styling across the app."""

    # ============================================================================
    # COLORS
    # ============================================================================

    # Primary Brand Color (consistent across themes)
    PRIMARY_GREEN = "#4CAF50"

    # Light Theme Colors (Burnt White Style)
    LIGHT_BACKGROUND = "#F8F9FA"  # Soft off-white, not pure white
    LIGHT_SURFACE = "#FFFFFF"  # Card backgrounds
    LIGHT_SURFACE_VARIANT = "#F1F3F4"  # Secondary surfaces
    LIGHT_BORDER = "#DEE2E6"  # Borders and dividers
    LIGHT_TEXT_PRIMARY = "#212529"  # Main text
    LIGHT_TEXT_SECONDARY = "#6C757D"  # Secondary text
    LIGHT_TEXT_TERTIARY = "#ADB5BD"  # Placeholder text

    # Dark Theme Colors (GitHub-inspired)
    DARK_BACKGROUND = "#0D1117"  # Main background (GitHub canvas)
    DARK_SURFACE = "#161B22"  # Card backgrounds (GitHub surface)
    DARK_SURFACE_VARIANT = "#21262D"  # Elevated surfaces
    DARK_BORDER = "#30363D"  # Borders and dividers
    DARK_TEXT_PRIMARY = "#E6EDF3"  # Main text
    DARK_TEXT_SECONDARY = "#8B949E"  # Secondary text
    DARK_TEXT_TERTIARY = "#6E7681"  # Placeholder text

    # Semantic Colors (consistent across themes)
    SUCCESS = "#4CAF50"
    ERROR = "#F44336"
    WARNING = "#FF9800"
    INFO = "#2196F3"
    DEFAULT_AVATAR_BG = "#9E9E9E"  # Fallback avatar background color
    TEXT_ON_COLORED_BG = (
        "#FFFFFF"  # White text on colored backgrounds (badges, tags, avatars)
    )

    # Interactive States
    HOVER_OVERLAY_LIGHT = "#00000010"  # 10% black overlay
    HOVER_OVERLAY_DARK = "#FFFFFF10"  # 10% white overlay

    # ============================================================================
    # ANIMATIONS & TRANSITIONS
    # ============================================================================

    # Animation Durations (in milliseconds)
    ANIMATION_DURATION_FAST = 200  # Fast transitions (hover effects, scale)
    ANIMATION_DURATION_MEDIUM = 300  # Medium transitions (dialogs, sheets)
    ANIMATION_DURATION_SLOW = 500  # Slow transitions (page transitions)

    # Photo Grid Hover Effects
    PHOTO_HOVER_SCALE = 1.05  # Scale factor on hover (5% enlargement)
    PHOTO_HOVER_SHADOW_BLUR = 8  # Shadow blur radius on hover
    PHOTO_HOVER_SHADOW_SPREAD = 2  # Shadow spread radius on hover
    PHOTO_HOVER_SHADOW_OFFSET_Y = 4  # Shadow vertical offset on hover
    PHOTO_DEFAULT_SHADOW_COLOR = "#00000000"  # Transparent shadow (default state)
    PHOTO_HOVER_SHADOW_COLOR_LIGHT = "#00000030"  # 30% black shadow (light mode hover)
    PHOTO_HOVER_SHADOW_COLOR_DARK = "#00000050"  # 50% black shadow (dark mode hover)

    # NavigationBar Colors (lighter for better readability)
    NAV_ICON_LIGHT = "#495057"  # Lighter than primary text for subtle icons
    NAV_ICON_DARK = "#C9D1D9"  # Lighter than primary text in dark mode
    NAV_LABEL_LIGHT = "#6C757D"  # Secondary text color
    NAV_LABEL_DARK = "#8B949E"  # Secondary text color in dark mode

    # ============================================================================
    # TYPOGRAPHY
    # ============================================================================

    # Font Sizes (in pixels)
    FONT_SIZE_TITLE = 24
    FONT_SIZE_SUBTITLE = 18
    FONT_SIZE_BODY = 14
    FONT_SIZE_CAPTION = 12
    FONT_SIZE_SMALL = 10

    # Font Weights
    FONT_WEIGHT_BOLD = ft.FontWeight.BOLD
    FONT_WEIGHT_MEDIUM = ft.FontWeight.W_500
    FONT_WEIGHT_NORMAL = ft.FontWeight.NORMAL

    # ============================================================================
    # SPACING & LAYOUT
    # ============================================================================

    SPACING_XXS = 2  # Extra-extra-small: tight micro-spacing for dense layouts
    SPACING_XS = 4
    SPACING_SM = 8
    SPACING_MD = 16
    SPACING_LG = 24
    SPACING_XL = 32

    # ============================================================================
    # ICON SIZES
    # ============================================================================

    ICON_SIZE_SM = 16
    ICON_SIZE_MD = 20
    ICON_SIZE_LG = 24
    ICON_SIZE_XL = 40

    # ============================================================================
    # COMPONENT DIMENSIONS
    # ============================================================================

    CARD_WIDTH_STANDARD = 450
    CARD_WIDTH_NARROW = 400
    CARD_WIDTH_PROFILE = 500  # Wider card for profile stats
    CARD_BORDER_RADIUS = 12
    CARD_ELEVATION = 3

    INPUT_FIELD_WIDTH = 300  # Standard width for form inputs
    BUTTON_HEIGHT = 50  # Standard button height
    BUTTON_WIDTH_MEDIUM = 200  # Medium width buttons (e.g., "Nova publicação")

    # Landing page specific
    LOGO_SIZE = 100  # Large logo text size
    LANDING_BUTTON_WIDTH = 150  # Width of action buttons on landing page
    LANDING_SPACER_HEIGHT = 30  # Spacing between logo and buttons

    # Avatar dimensions
    AVATAR_SIZE_SMALL = 32
    AVATAR_SIZE_MEDIUM = 48
    AVATAR_SIZE_LARGE = 64
    AVATAR_RADIUS_SMALL = 16  # Small avatar radius (comments, compact views)
    AVATAR_RADIUS_LARGE = 50  # Large avatar radius (profile page, circular)

    # Post card specific
    POST_IMAGE_HEIGHT = 200  # Standard height for post card images
    DIVIDER_HEIGHT = 1  # Thin divider line

    # Navigation badge
    BADGE_SIZE = 24  # Small badge for notification count

    # ============================================================================
    # DIALOG DIMENSIONS (Responsive)
    # ============================================================================

    # Dialog responsive sizes - three fixed breakpoints
    DIALOG_WIDTH_SMALL = 400  # Mobile/compact devices
    DIALOG_WIDTH_MEDIUM = 600  # Tablets/small desktops
    DIALOG_WIDTH_LARGE = 800  # Large desktops

    DIALOG_HEIGHT_SMALL = 500  # Compact dialogs
    DIALOG_HEIGHT_MEDIUM = 600  # Standard dialogs
    DIALOG_HEIGHT_LARGE = 700  # Extended content dialogs

    # Dialog content constraints
    DIALOG_CONTENT_MAX_HEIGHT_SMALL = 400  # Scrollable content height for small dialogs
    DIALOG_CONTENT_MAX_HEIGHT_MEDIUM = (
        500  # Scrollable content height for medium dialogs
    )
    DIALOG_CONTENT_MAX_HEIGHT_LARGE = 600  # Scrollable content height for large dialogs

    # Dialog image heights
    DIALOG_IMAGE_HEIGHT = 300
    DIALOG_RELATED_IMAGE_HEIGHT = 150

    # Dialog padding constants (standardized for all dialogs)
    DIALOG_TITLE_PADDING = SPACING_SM  # Padding around dialog title row (8px)
    DIALOG_CONTENT_PADDING = SPACING_MD  # Main content area padding (16px)
    DIALOG_INSET_PADDING = SPACING_LG  # Internal component padding (24px)
    DIALOG_ACTIONS_PADDING = SPACING_SM  # Actions button area padding (8px)

    # ============================================================================
    # COMPONENT-SPECIFIC SPACING
    # ============================================================================

    # Badge (notification count in navigation bar)
    BADGE_BORDER_RADIUS = 10
    BADGE_PADDING_HORIZONTAL = 5
    BADGE_PADDING_VERTICAL = 2

    # Tag chips (post cards, search filters)
    TAG_PADDING_HORIZONTAL = 10
    TAG_PADDING_VERTICAL = 5

    # Comments
    COMMENT_INDENT = 40  # Left indent for nested "view more" button

    # Borders
    BORDER_WIDTH_STANDARD = 2  # Standard border width for buttons, containers

    # ============================================================================
    # TEXT STYLES (Helper Functions)
    # ============================================================================

    @staticmethod
    def title_style(is_dark_mode=False):
        """Title text style (24px, bold)"""
        return ft.TextStyle(
            size=AppTheme.FONT_SIZE_TITLE,
            weight=AppTheme.FONT_WEIGHT_BOLD,
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
        )

    @staticmethod
    def subtitle_style(is_dark_mode=False):
        """Subtitle text style (18px, medium)"""
        return ft.TextStyle(
            size=AppTheme.FONT_SIZE_SUBTITLE,
            weight=AppTheme.FONT_WEIGHT_MEDIUM,
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
        )

    @staticmethod
    def body_style(is_dark_mode=False):
        """Body text style (14px, normal)"""
        return ft.TextStyle(
            size=AppTheme.FONT_SIZE_BODY,
            weight=AppTheme.FONT_WEIGHT_NORMAL,
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
        )

    @staticmethod
    def caption_style(is_dark_mode=False):
        """Caption text style (12px, normal, secondary color)"""
        return ft.TextStyle(
            size=AppTheme.FONT_SIZE_CAPTION,
            weight=AppTheme.FONT_WEIGHT_NORMAL,
            color=(
                AppTheme.DARK_TEXT_SECONDARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_SECONDARY
            ),
        )

    # ============================================================================
    # COMPONENT HELPERS
    # ============================================================================

    @staticmethod
    def get_card_container(content, is_dark_mode=False, width=None):
        """
        Returns a standardized Card container with consistent styling.

        Args:
            content: The content to display inside the card
            is_dark_mode: Whether to use dark theme styling
            width: Optional width override (defaults to CARD_WIDTH_STANDARD)
        """
        return ft.Container(
            content=content,
            width=width or AppTheme.CARD_WIDTH_STANDARD,
            bgcolor=AppTheme.DARK_SURFACE if is_dark_mode else AppTheme.LIGHT_SURFACE,
            border_radius=AppTheme.CARD_BORDER_RADIUS,
            padding=AppTheme.SPACING_MD,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color="#00000020" if not is_dark_mode else "#00000040",
                offset=ft.Offset(0, 2),
            ),
        )

    @staticmethod
    def get_elevated_button(
        text, on_click, is_dark_mode=False, width=None, height=None
    ):
        """
        Returns a standardized elevated button with consistent styling.

        Args:
            text: Button text
            on_click: Click handler function
            is_dark_mode: Whether to use dark theme styling
            width: Optional width override
            height: Optional height override
        """
        return ft.ElevatedButton(
            content=text,
            on_click=on_click,
            width=width,
            height=height,
            bgcolor=AppTheme.PRIMARY_GREEN,
            color="#FFFFFF",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=AppTheme.CARD_BORDER_RADIUS)
            ),
        )

    @staticmethod
    def get_text_button(text, on_click, is_dark_mode=False):
        """
        Returns a standardized text button.

        Args:
            text: Button text
            on_click: Click handler function
            is_dark_mode: Whether to use dark theme styling
        """
        return ft.TextButton(
            content=text,
            on_click=on_click,
            style=ft.ButtonStyle(color=AppTheme.PRIMARY_GREEN),
        )

    @staticmethod
    def get_input_field(
        label, hint_text=None, password=False, is_dark_mode=False, **kwargs
    ):
        """
        Returns a standardized input field with consistent styling.

        Args:
            label: Field label
            hint_text: Optional placeholder text
            password: Whether this is a password field
            is_dark_mode: Whether to use dark theme styling
            **kwargs: Additional TextField properties
        """
        return ft.TextField(
            label=label,
            hint_text=hint_text,
            password=password,
            border_radius=AppTheme.CARD_BORDER_RADIUS,
            bgcolor=(
                AppTheme.DARK_SURFACE_VARIANT
                if is_dark_mode
                else AppTheme.LIGHT_SURFACE_VARIANT
            ),
            border_color=(
                AppTheme.DARK_BORDER if is_dark_mode else AppTheme.LIGHT_BORDER
            ),
            focused_border_color=AppTheme.PRIMARY_GREEN,
            color=(
                AppTheme.DARK_TEXT_PRIMARY
                if is_dark_mode
                else AppTheme.LIGHT_TEXT_PRIMARY
            ),
            **kwargs
        )

    @staticmethod
    def get_divider(is_dark_mode=False):
        """Returns a themed divider."""
        return ft.Divider(
            height=1,
            color=AppTheme.DARK_BORDER if is_dark_mode else AppTheme.LIGHT_BORDER,
        )

    # ============================================================================
    # RESPONSIVE HELPERS (explore page)
    # ============================================================================

    @staticmethod
    def get_responsive_container_width(window_width: int) -> int:
        """
        Returns a fixed container width based on responsive breakpoints.

        Breakpoints:
        - < 600px      -> CARD_WIDTH_STANDARD (450px)
        - 600 - 900px  -> 600px
        - > 900px      -> 800px

        Args:
            window_width: Current window width in pixels

        Returns:
            int: Container width in pixels according to the breakpoints
        """
        if window_width is None:
            # Sensible default if width is unknown
            return AppTheme.CARD_WIDTH_STANDARD

        if window_width < 600:
            return AppTheme.CARD_WIDTH_STANDARD
        elif window_width < 900:
            return 600
        else:
            return 800

    @staticmethod
    def get_responsive_dialog_size(window_width: int | None = None) -> tuple[int, int]:
        """
        Returns appropriate dialog width and height based on responsive breakpoints.

        Three fixed size tiers:
        - Small:  400px × 500px  (< 600px window width)
        - Medium: 600px × 600px  (600-900px window width)
        - Large:  800px × 700px  (> 900px window width)

        Args:
            window_width: Current window width in pixels (optional)

        Returns:
            tuple[int, int]: (dialog_width, dialog_height) in pixels
        """
        if window_width is None or window_width < 600:
            return (AppTheme.DIALOG_WIDTH_SMALL, AppTheme.DIALOG_HEIGHT_SMALL)
        elif window_width < 900:
            return (AppTheme.DIALOG_WIDTH_MEDIUM, AppTheme.DIALOG_HEIGHT_MEDIUM)
        else:
            return (AppTheme.DIALOG_WIDTH_LARGE, AppTheme.DIALOG_HEIGHT_LARGE)

    @staticmethod
    def get_dialog_content_height(window_width: int | None = None) -> int:
        """
        Returns appropriate scrollable content height for dialogs based on breakpoints.

        Ensures content area is scrollable within fixed dialog dimensions.

        Args:
            window_width: Current window width in pixels (optional)

        Returns:
            int: Maximum content height in pixels for scrollable area
        """
        if window_width is None or window_width < 600:
            return AppTheme.DIALOG_CONTENT_MAX_HEIGHT_SMALL
        elif window_width < 900:
            return AppTheme.DIALOG_CONTENT_MAX_HEIGHT_MEDIUM
        else:
            return AppTheme.DIALOG_CONTENT_MAX_HEIGHT_LARGE


# ============================================================================
# THEME DEFINITIONS FOR FLET APP
# ============================================================================


def get_light_theme():
    """
    Returns Flet Theme for light mode.
    Burnt white background with soft grays for professional appearance.
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppTheme.PRIMARY_GREEN,
            on_primary="#FFFFFF",
            secondary=AppTheme.LIGHT_TEXT_SECONDARY,
            on_secondary="#FFFFFF",
            surface=AppTheme.LIGHT_SURFACE,
            on_surface=AppTheme.LIGHT_TEXT_PRIMARY,
            error=AppTheme.ERROR,
            on_error="#FFFFFF",
        ),
        # Use system font stack for optimal rendering
        font_family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    )


def get_dark_theme():
    """
    Returns Flet Theme for dark mode.
    GitHub-inspired dark theme with subtle contrasts and variations of gray.
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppTheme.PRIMARY_GREEN,
            on_primary="#FFFFFF",
            secondary=AppTheme.DARK_TEXT_SECONDARY,
            on_secondary="#FFFFFF",
            surface=AppTheme.DARK_SURFACE,
            on_surface=AppTheme.DARK_TEXT_PRIMARY,
            error=AppTheme.ERROR,
            on_error="#FFFFFF",
        ),
        font_family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    )


# Default theme (can be changed based on user preference or system setting)
default_theme = get_light_theme()
