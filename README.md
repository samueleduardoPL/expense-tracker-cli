# Expense Tracker CLI

A simple command-line expense tracker built with Python, following a layered architecture and including unit tests.

---

## Overview

This project allows users to:

- Add expenses
- Store data persistently in JSON files
- Validate domain rules
- Run automated tests

It was built to practice:

- Clean project structure (`src` layout)
- Separation of concerns (UI, Domain, Data)
- Input validation
- Unit testing with `pytest`

Proyect especifications found at: https://roadmap.sh/projects/expense-tracker

---

## Project Structure

```
expense-tracker-cli/
│
├── src/
│   └── expensetracker/
│       ├── domain/
│       ├── data/
│       ├── ui/
│       └── main.py
│
├── tests/
│   └── test_expense.py
│
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/samueleduardoPL/expense-tracker-cli.git
cd expense-tracker-cli
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependencies:

```bash
pip install pytest
```

---

## Running the Application

From the project root:

```bash
$env:PYTHONPATH="src"
python -m expensetracker.main
```

---

## Running Tests

```bash
$env:PYTHONPATH="src"
pytest
```

Tests currently cover:

- Valid expense creation
- Empty description validation
- Negative amount validation
- Amount type validation

---

## Design Decisions

- Used a `src/` layout to avoid accidental imports from the project root.
- Separated layers into Domain, Data, and UI for better maintainability.
- Implemented validation inside the domain entity to enforce business rules.
- Added unit tests to prevent regressions.

---

## Author

Samuel Polanco  
Backend-focused software engineering student
