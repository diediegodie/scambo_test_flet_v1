# 🔄 SCAMBO

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

### Current Features (Frontend Complete)

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

### Coming Soon (Backend Integration)

- User authentication with JWT
- Real-time data from API
- Post creation and management
- Comment system
- Trade proposals
- Notification system
- User reputation system

---

## Tech Stack

### Frontend
- **[Flet](https://flet.dev/)** - Python framework for building multi-platform UIs
- **Python 3.11+** - Modern Python with type hints

### Backend (Planned)
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for APIs
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - SQL toolkit and ORM
- **[Alembic](https://alembic.sqlalchemy.org/)** - Database migration tool
- **[PostgreSQL](https://www.postgresql.org/)** - Robust relational database

### Development Tools
- **Black** - Code formatting
- **Flake8** - Style checking
- **Mypy** - Type checking
- **Pytest** - Testing framework

---

## Project Status

### Completed
- **Frontend**: 100% complete with all pages and features
- **Design System**: Centralized theme with 86+ constants
- **Mock Data**: Complete data layer for all features
- **Documentation**: Comprehensive guides and technical docs
- **Code Quality**: Zero hardcoded values, 100% theme compliance

### In Progress
- Backend API development (FastAPI + PostgreSQL)

### Planned
- Authentication system
- Database models and migrations
- API endpoints for all features
- Integration with frontend
- Production deployment

---

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/diediegodie/scambo_test_flet_v1.git
   cd scambo_test_flet_v1
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development tools (optional)**
   ```bash
   pip install black flake8 mypy pytest
   ```

---

## Usage

### Running the Application

**Standard method:**
```bash
python3 run_app.py
```

**Using Flet CLI (for mobile development):**
```bash
flet run --android  # For Android
flet run --ios      # For iOS
```

**Alternative entry point:**
```bash
python3 main.py
```

### Theme Configuration

To launch the app in dark mode:
1. Open `run_app.py`
2. Change `is_dark_mode = False` to `is_dark_mode = True`
3. Run the application

Theme preferences are automatically saved in client storage and persist across sessions.

### Development Mode

For development with hot reload:
```bash
flet run --web run_app.py
```

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
│       │   └── notification_detail_dialog.py  # Notification detail
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
│   └── initial docs/              # Technical specs
│
├── tests/                # Test suite
│   ├── test_navigation.py
│   ├── test_new_dialog.py
│   └── test_perfil.py
│
├── main.py               # Entry point (Flet CLI)
├── run_app.py            # Main entry point
└── requirements.txt      # Python dependencies
```

### Key Directories Explained

- **`frontend/ui/pages/`** - All page modules (landing, auth, dashboard, etc.)
- **`frontend/ui/widgets/`** - Reusable UI components
- **`frontend/ui/theme.py`** - Single source of truth for all styling
- **`mock/`** - Mock data providers with API-ready structure
- **`backend/`** - Backend structure (scaffolded, awaiting implementation)
- **`docs/`** - Comprehensive project documentation

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

### Data Flow

**Current (Mock Data):**
```
Page → Mock Provider → Dict[str, Any] → UI Component
```

**Future (API Integration):**
```
Page → API Client → FastAPI Endpoint → Service → Model → Database
                                                    ↓
Page ← Pydantic Schema ← API Response ← Service ← Model
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **[Flet Team](https://flet.dev/)** - For the amazing Python UI framework
- **[FastAPI](https://fastapi.tiangolo.com/)** - For the modern web framework
- **Community Contributors** - For feedback and support

---

## Contact

For questions, suggestions, or support:

- **Project Repository:** [GitHub](https://github.com/diediegodie/scambo_test_flet_v1)
- **Issues:** [Issue Tracker](https://github.com/diediegodie/scambo_test_flet_v1/issues)

---

## Project Stats

- **Total Files:** 50+
- **Lines of Code:** ~6,000+
- **UI Pages:** 8
- **Reusable Widgets:** 7
- **Theme Constants:** 86+
- **Mock Data Providers:** 4
- **Test Coverage:** In Progress
- **Documentation Pages:** 10+
