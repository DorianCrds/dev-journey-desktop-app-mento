# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project follows Semantic Versioning.

---

## [Unreleased]

### Planned
- Unit tests for services, repositories, and domain models
- Improved validation and error feedback in forms
- Import / export support for local knowledge data
- Optional database backup and restore workflow
- Installer versioning workflow improvements

---

## [v1.0.0] - Initial stable release

### Added
- Desktop GUI application built with PySide6
- Notion management with create, read, update, and delete workflows
- Category management for organizing notions
- Tag management and notion/tag associations
- Automatic notion status based on description completion
- Search by notion title or description
- Category-based notion filtering
- Dashboard with global learning statistics
- Pie chart for acquired vs to-learn distribution
- Bar chart for progression by top categories
- Light and dark theme selection from the settings page
- Local SQLite persistence with schema initialization
- User data directory storage for the application database
- Windows executable packaging with PyInstaller
- Windows installer packaging with Inno Setup

### Technical details
- Layered desktop architecture with:
  - views
  - presenters
  - services
  - domain models
  - repositories and mappers
- MVP-inspired separation between UI events and application logic
- Shared event system for cross-view refreshes
- Local `qute` package for theme management, QSS templating, design tokens, and fonts
- PyInstaller spec file bundling application assets, database resources, and theme files

### Notes
- Fully offline by design
- Local and single-user only
- No account, authentication, or network service required
- Designed as a learning-focused desktop application project
