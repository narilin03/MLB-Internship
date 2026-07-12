# Day 2: Python Data Structures & Student Record Management System

A command-line console application that handles primitive Python collection objects, performs raw calculations, and manages a mock student database in memory.

## What It Does
- Processes core mathematical operations on raw lists, tuples, and sets.
- Adds, reads, searches, updates, and deletes data inside a live terminal workspace.
- Validates user input entries to prevent crashes from bad data formats.
- Tracks live database registration counters dynamically across runtime cycles.

## Features
- **Add Student**: Registers custom name, age, and course information under a unique roll number.
- **View All Students**: Loops through memory profiles and formats active records on the screen.
- **Search Student**: Scans records via linear search matching to pull out target profiles.
- **Update Student**: Overwrites individual fields or leaves them unchanged by hitting Enter.
- **Delete Student**: Deletes an active registration profile out of memory cleanly using `.pop()`.

## Core Logic & Validation
- **No Built-in Shortcuts**: Algorithms run completely without shorthand operations like `max()`, `min()`, or `.count()`.
- **Type Guarding**: Verifies numeric inputs natively using `.isdigit()` to safely convert text fields into integers.
- **Uniqueness Check**: Loops through keys automatically to block identical roll numbers from corrupting the dataset.

## Concepts Practiced
- Functions & Scope
- Lists & Parallel Loops
- Dictionary Mapping (`.items()`)
- String Processing (`.split()`, `.lower()`)
- In-Memory State Retention
- Menu-Driven Application Design

## Files
- `practice_problems.py`: Code implementations covering lists, tuples, sets, and basic dictionaries.
- `student_management.py`: Source code for the interactive Student Record Management System.
