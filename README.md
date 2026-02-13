# SCAMBO

**Safe Exchanges Between People**

A social network platform for secure bartering and trading of goods and services without using money.

[![Status](https://img.shields.io/badge/Status-Frontend%20Complete-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![Flet](https://img.shields.io/badge/Flet-Latest-purple)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Status](#project-status)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development](#development)
- [Roadmap](#roadmap)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

---

## About

SCAMBO is an application that enables people to exchange products and services with each other in a safe and reliable way. Whether it's trading guitar lessons for English lessons, or a smartphone for a bicycle, SCAMBO provides a secure platform to make exchanges without the risk of being scammed.

### Key Concept

The app creates multiple barriers against scams through:
- **Identity Verification** (basic for everyone, enhanced for high-value exchanges)
- **Visual Proof** of items/services (photos and videos)
- **Financial Guarantee System** (deposit system)
- **User Ratings** after each exchange
- **Progressive Trust System** (new users start with lower-value exchanges)
- **Conflict Mediation** (complaint system with evidence analysis)

### Who Is It For?

Anyone who wants to make exchanges without using money, whether physical objects or services like lessons, repairs, or creative work.

---

## Features

### Current Features

#### Core Pages
- **Landing Page** - Welcome screen with logo and call-to-action buttons
- **Authentication** - Login and account creation flows
- **Dashboard** - Full-screen scrolling feed with rich post cards
- **Profile** - User information, stats, and personal post feed
- **Search/Explore** - Photo grid with filters, pagination, and keyboard navigation
- **Notifications** - Real-time notification center with detail modals
- **Settings** - App configuration including theme switching

#### UI Components
- **Post Cards** - Images, descriptions, tags, comments, and interaction buttons
- **Navigation Bar** - Bottom navigation with notification badges
- **Dialogs** - Reusable modals for post details, notifications, and new posts
- **Theme System** - Dark/Light mode with 86+ centralized design tokens
- **Responsive Design** - Adapts to mobile, tablet, and desktop screens

#### Technical Features
- **Mock Data Layer** - Complete data providers for backend-ready architecture
- **Theme Persistence** - User preferences saved across sessions
- **Accessibility** - WCAG AA compliant contrast ratios
- **Zero Hardcoded Values** - All styling centralized in theme system
- **Clean Architecture** - Clear separation of concerns (UI/Widgets/Data)

---

## Tech Stack

### Frontend
- **[Flet](https://flet.dev/)**
- **Python 3.11+**

### Backend (Planned)
- **[FastAPI](https://fastapi.tiangolo.com/)**
- **[SQLAlchemy](https://www.sqlalchemy.org/)**
- **[Alembic](https://alembic.sqlalchemy.org/)**
- **[PostgreSQL](https://www.postgresql.org/)**

### Development Tools
- **Black** - Code formatting
- **Flake8** - Style checking
- **Mypy** - Type checking
- **Pytest** - Testing framework

---

## Project Structure

```
scambo_test_flet_v1/
├── frontend/               # Frontend code (Flet UI)
│   ├── assets/            # Images and static files
│   └── ui/                # UI components and pages
│       ├── pages/         # Page modules (8 pages)
│       │   ├── index.py              # Landing page
│       │   ├── login.py              # Login page
│       │   ├── create_account.py    # Registration
│       │   ├── dashboard.py         # Main feed
│       │   ├── perfil.py            # Profile page
│       │   ├── search.py            # Search/explore
│       │   ├── notifications.py     # Notifications
│       │   └── configurations.py    # Settings
│       ├── widgets/       # Reusable components (7 widgets)
│       │   ├── nav_bar.py           # Bottom navigation
│       │   ├── post_card.py         # Post feed item
│       │   ├── notification_card.py # Notification item
│       │   ├── new_post_dialog.py   # Create post modal
│       │   ├── post_detail_dialog.py     # Post detail modal
│       │   └── notification_detail_dialog.py  # Notification detail modal
│       ├── state/         # (Reserved for future state management)
│       ├── utils/         # (Reserved for future utilities)
│       └── theme.py       # Centralized design system (86+ constants)
│
├── backend/               # Backend code (FastAPI) - Structure ready
│   ├── api/              # API routes
│   ├── core/             # Config, security, dependencies
│   ├── db/               # Database connection
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   └── services/         # Business logic
│
├── mock/                 # Mock data providers (backend-ready)
│   ├── posts.py          # Post data and helpers
│   ├── user.py           # User data
│   ├── comments.py       # Comment data
│   └── notifications.py  # Notification data
│
├── docs/                 # Documentation
│   ├── project_overview.md        # Project summary
│   ├── memorie.md                 # Development history
│   ├── VERIFICATION_REPORT.md     # Code audit report
│   ├── initial docs/              # Technical specifications
│   │   ├── api_flows.md          # API flow diagrams
│   │   ├── app_summary.md        # App overview
│   │   ├── onboarding.md         # Onboarding flow
│   │   ├── security_.md          # Security guidelines
│   │   ├── technical_requirements.md
│   │   └── technical_tickets_roadmap.md
│   └── ui/                        # UI documentation
│       ├── filter_and_pagination_implementation.md
│       └── theme_consistency_report.md
│
├── tests/                # Test suite
│   ├── test_navigation.py
│   ├── test_new_dialog.py
│   └── test_perfil.py
│
├── main.py               # Entry point (Flet CLI)
├── run_app.py            # Main entry point
├── requirements.txt      # Python dependencies
└── storage/              # Persistent storage (data/temp)
```

### Key Directories Explained

- **`frontend/ui/pages/`** - All page modules (8 pages: landing, auth, dashboard, profile, search, notifications, settings)
- **`frontend/ui/widgets/`** - Reusable UI components (nav bar, post card, dialogs, etc.)
- **`frontend/ui/state/`** - Reserved for future state management (currently empty)
- **`frontend/ui/utils/`** - Reserved for future utility functions (currently empty)
- **`frontend/ui/theme.py`** - Single source of truth for all styling (86+ design tokens)
- **`backend/`** - Backend structure (FastAPI + SQLAlchemy, scaffolded and ready for implementation)
- **`mock/`** - Mock data providers with API-ready structure (posts, users, comments, notifications)
- **`docs/`** - Comprehensive project documentation including technical specs and UI reports
- **`storage/`** - Persistent data storage (data/ for files, temp/ for temporary data)
- **`tests/`** - Test suite with navigation, dialog, and profile tests

---

## Development

### Development Guidelines

This project follows strict development rules to maintain code quality and consistency.

#### Key Principles

1. **Clean Architecture** - Clear separation of concerns
2. **No Hardcoded Values** - All styling in `theme.py`
3. **Mock Data Layer** - Backend-ready architecture
4. **Component Reusability** - DRY principle throughout
5. **Type Hints** - Modern Python with full type annotations
6. **Documentation** - Clear docstrings and comments

---

## Architecture

### Frontend Architecture

**Pattern:** Component-based with centralized theming

```
┌─────────────────────────────────────────┐
│           Entry Point (run_app.py)      │
│    - Theme initialization               │
│    - Client storage setup               │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│            Pages Layer                  │
│  - index.py (Landing)                   │
│  - login.py / create_account.py         │
│  - dashboard.py (Main feed)             │
│  - perfil.py (Profile)                  │
│  - search.py (Explore)                  │
│  - notifications.py                     │
│  - configurations.py (Settings)         │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│          Widgets Layer                  │
│  - PostCard (Feed item)                 │
│  - NotificationCard (Notification item) │
│  - NavigationBar (Bottom nav)           │
│  - Dialogs (Modals)                     │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│         Theme System (theme.py)         │
│  - 86+ centralized constants            │
│  - Dark/Light mode definitions          │
│  - Helper functions                     │
└─────────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│        Mock Data Layer (mock/)          │
│  - posts.py (Post data)                 │
│  - user.py (User data)                  │
│  - comments.py (Comment data)           │
│  - notifications.py (Notification data) │
└─────────────────────────────────────────┘
```

### Backend Architecture (Planned)

**Pattern:** Clean Architecture with FastAPI

```
┌─────────────────────────────────────────┐
│          API Layer (api/)               │
│  - Route handlers                       │
│  - Request/Response models              │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│        Services Layer (services/)       │
│  - Business logic                       │
│  - Data processing                      │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│         Models Layer (models/)          │
│  - SQLAlchemy models                    │
│  - Database schema                      │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│        Database Layer (db/)             │
│  - Connection management                │
│  - Session handling                     │
└─────────────────────────────────────────┘
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or support:

- **Project Repository:** [GitHub](https://github.com/diediegodie/scambo_test_flet_v1)
- **Issues:** [Issue Tracker](https://github.com/diediegodie/scambo_test_flet_v1/issues)