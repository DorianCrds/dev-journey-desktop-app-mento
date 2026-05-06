# Mento - Desktop Knowledge Tracker

This project is part of my **Dev Journey**, a structured, project-based exploration
of the main types of software development.

[View Dev Journey GitHub 'Hub' repository](https://github.com/DorianCrds/dev-journey)

---

## Project goals

The goal of this project is to build a **local desktop application** designed to help track, structure, and review technical knowledge acquired during a developer journey.

This project focuses on:
- building a classic desktop GUI application
- structuring a Python desktop app with clear layers
- managing local application state and user-driven events
- persisting structured data locally with SQLite
- visualizing learning progress through a dashboard
- packaging a Windows desktop application for distribution

The application is intentionally scoped to remain **small, local, offline, and single-user**, in line with the educational goals of the Dev Journey.

---

## Features

- Create, read, update, and delete **notions** (technical knowledge items)
- Each notion includes:
  - a title
  - a category
  - an optional context (where / how the notion was encountered)
  - an optional description
  - an automatic learning status:
    - *À apprendre*
    - *Acquise*
- A notion becomes *acquired* once its description is completed
- Manage categories separately
- Manage tags separately and associate them with notions
- Search notions by title or description
- Filter notions by category
- Visual dashboard displaying:
  - total number of notions
  - acquired vs non-acquired notions
  - overall progression percentage
  - acquired / to-learn distribution chart
  - progression by top categories
- Settings page with light and dark theme selection
- Local data persistence using SQLite
- Fully offline usage, with no account or network requirement

---

## Usage

The application is a local desktop program intended to be launched directly by the user.

Typical usage:
- Create a new notion when encountering an unfamiliar concept
- Add contextual information about where the notion was discovered
- Link the notion to a category and optional tags
- Complete the description once the concept is understood
- Use search and filters to retrieve existing notions
- Track progress visually through the dashboard

No network connection or account is required.

---

## How to run locally

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Launch the application:

```bash
python run_mento.py
```

The app creates its local SQLite database in the user data directory:
- Windows: `%LOCALAPPDATA%\Mento\database\mento.db`
- macOS: `~/Library/Application Support/Mento`
- Linux: `$XDG_DATA_HOME/Mento` or `~/.local/share/Mento`

To test the main flow manually:
- create a category and a tag
- create a notion linked to that category and tag
- edit the notion and add a description
- check that its status changes to *Acquise*
- use search and category filtering from the notions page
- open the dashboard and verify that the statistics and charts update
- switch between light and dark themes from the settings page

---

## How it works

- The application uses a **local SQLite database** to store:
  - notions
  - categories
  - tags
  - notion/tag relationships
- The app follows a layered desktop architecture:
  - views define the PySide6 UI
  - presenters connect UI events to application actions
  - services hold application logic and DTO conversion
  - domain models represent core entities
  - repositories and mappers handle SQLite persistence
- A shared event object coordinates refreshes between screens
- The dashboard computes statistics from stored data using aggregation queries
- The local `qute` package provides the theme system, QSS templates, design tokens, fonts, and reusable theme widgets.
  Its standalone repository is available here: [DorianCrds/qute](https://github.com/DorianCrds/qute)

The application is designed to be:
- event-driven
- stateful
- fully offline
- packaged as a Windows desktop application

---

## Project structure

```bash
.
├── app/
│   ├── core/               # Shared application events
│   ├── domain/             # Core models (Notion, Category, Tag)
│   ├── persistence/        # SQLite connector, repositories, and mappers
│   ├── presenters/         # Presentation logic between views and services
│   ├── services/           # Application logic and DTOs
│   ├── utils/              # Paths and logging helpers
│   └── views/              # PySide6 windows, pages, and reusable components
├── assets/                 # Application assets, including icon/logo
├── database/               # SQLite schema and seed data
├── installer/              # Inno Setup script and generated installer output
├── qute/                   # Local theme/design-system package for PySide6
├── CHANGELOG.md
├── Mento.spec              # PyInstaller build specification
├── requirements.txt
├── run_mento.py            # Application entry point
└── README.md
```

---

## Packaging

The Windows executable is built with **PyInstaller** from the project spec file.
The spec bundles the application entry point, assets, database schema, and `qute` theme resources.

Build a fresh executable from `Mento.spec`:

```bash
pyinstaller --clean --noconfirm Mento.spec
```

The generated application is placed in:

```bash
dist\Mento\Mento.exe
```

The Windows installer is then produced with **Inno Setup** from:

```bash
installer\Mento.iss
```

Compile this script with Inno Setup after the PyInstaller build. The installer output is generated in:

```bash
installer\output\MentoSetup-<version>.exe
```

When releasing a new version, update the version in `installer\Mento.iss` before compiling the installer, using Inno Setup Compiler software (for free).

---

## Technologies used

- Python
- PySide6 (Qt for Python) for the graphical user interface
- Qt Charts for dashboard visualizations
- SQLite for local data persistence
- Jinja2 for QSS stylesheet templating
- PyInstaller for Windows executable packaging
- Inno Setup for Windows installer generation

No network access or external services are required at runtime.

---

## Key concepts practiced

- Desktop GUI development with PySide6
- Event-driven programming with signals and slots
- MVP-inspired separation between views, presenters, services, and persistence
- Application state management
- Relational data modeling with SQLite
- Local data persistence in a user data directory
- Data aggregation for dashboard statistics
- Theme management with QSS, JSON theme files, and reusable design tokens
- Desktop packaging with PyInstaller and Inno Setup

---

## Scope and limitations

This project is intentionally limited to keep the focus on core desktop concepts.

In scope:
- Local, single-user application
- Offline usage
- Basic CRUD operations
- Search and category-based filtering
- Simple dashboard statistics
- Windows executable and installer packaging

Out of scope:
- Authentication or user accounts
- Cloud synchronization
- Multi-device support
- Advanced analytics or history tracking
- Collaboration features

---

## What I learned

This project is intended to reinforce:
- how desktop applications differ from CLI and web applications
- how UI state and data persistence interact
- how to model and query structured local data
- how to organize a Python desktop app into maintainable layers
- how to build a small local design system for a PySide6 application
- how to package and distribute a desktop application on Windows
- how to scope a project realistically while keeping it useful

---

## Versioning

This project follows Semantic Versioning.
- v1.0.0 - Initial stable desktop application with core features and Windows packaging

---

# How this fits into my dev journey

Mento represents my first classic desktop application in the Dev Journey.

It bridges the gap between:
- command-line tools (previous projects)
- backend and full-stack applications (upcoming projects)

This project focuses on understanding:
- graphical interfaces
- user-driven workflows
- local application architecture
- local persistence and stateful desktop behavior
- desktop packaging and distribution

It serves as a foundation for more complex, stateful applications later in the journey.
