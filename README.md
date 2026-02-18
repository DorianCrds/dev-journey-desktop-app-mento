# Mento — Desktop Knowledge Tracker

This project is part of my **Dev Journey**, a structured, project-based exploration  
of the main types of software development.

[View Dev Journey GitHub 'Hub' repository](https://github.com/DorianCrds/dev-journey)

---

## Project goals

The goal of this project is to build a **simple desktop application** designed to help track and structure technical knowledge acquired during a developer journey.

This project focuses on:
- building a classic desktop GUI application
- managing local application state
- persisting structured data locally
- handling user-driven events
- visualizing data through a basic dashboard

The application is intentionally scoped to remain **small, local, and single-user**, in line with the educational goals of the Dev Journey.

---

## Features

- Create and manage **notions** (technical knowledge items)
- Each notion includes:
  - a title
  - an optional context (where / how the notion was encountered)
  - a description
  - a learning status:
    - *To learn*
    - *Acquired*
- Mark a notion as *acquired* once its description is completed
- Categorize notions using predefined categories
- Manage categories separately (add new categories as needed)
- Visual dashboard displaying:
  - total number of notions
  - number of acquired vs non-acquired notions
  - distribution of notions by category (chart)
- Local data persistence using a relational database
- Tag system to refine classification (e.g. "React", "Docker")
- Filtering notions by category or tag

---

## Usage

The application is a local desktop program intended to be launched directly by the user.

Typical usage:
- Create a new notion when encountering an unfamiliar concept
- Add contextual information about where the notion was discovered
- Complete the description once the concept is understood
- Track progress visually through the dashboard

No network connection or account is required.

---

## How it works

- The application uses a **local SQLite database** to store:
  - notions
  - categories
  - tags
  - relationships between them
- User interactions (button clicks, form inputs, selections) trigger events that:
  - update application state
  - persist data to the database
  - refresh the UI accordingly
- The dashboard view computes statistics directly from the stored data using aggregation queries

The application is designed to be:
- event-driven
- stateful
- fully offline

---

## Project structure

```bash
.
├── app/                    # Application entry point
├── ui/                     # UI main_components and views (PySide6)
├── domain/                 # Core data models (Notion, Category, Tag)
├── persistence/            # SQLite database access and queries
├── assets/                 # Static assets (icons, styles, etc.)
├── CHANGELOG.md
└── README.md
```
(Structure may evolve during implementation.)

---

## Technologies used

- Python
- PySide6 (Qt for Python) for the graphical user interface
- SQLite for local data persistence
- Python standard library (sqlite3)

No network access or external services are required.

---

## Key concepts practiced
- Desktop GUI development with PySide6
- Event-driven programming (signals and slots)
- Application state management
- Relational data modeling
- Local data persistence with SQLite
- Data aggregation for dashboard statistics
- Separation of concerns between UI, domain logic, and persistence

---

## Scope and limitations
This project is intentionnally limited to keep the focus on core desktop concepts.

In scope:
- Local, single-user application
- Offline usage
- Basic CRUP operations
- Simple dashboard statistics

Out of scope:
- Authentification or user accounts
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
- how to design a small but coherent desktop application
- how to scope a project realistically while keeping it useful

---

## Versioning
This project follows Semantic Versioning.
- v1.x.x - Initial desktop application with core features

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

It serves as a foundation for more complex, stateful applications later in the journey.
