# Day 1: Student Grading System

A command-line Python program that collects student academic profiles, processes numeric scores, and automatically evaluates letter grades.

## What It Does
- Takes dynamic console input for one or more students: Name, Class, and multiple matching Marks.
- Manually calculates each student's average score across their entered subject inputs.
- Assigns an absolute academic letter grade based on the final calculated average.
- Prints a clean, formatted transcript directly to the terminal screen.

## Grade Criteria

| Average Marks | Grade |
| --- | --- |
| 80 and above | A |
| 70 to 79.99 | B |
| 60 to 69.99 | C |
| Below 60 | D |

## Functions Used
- `input_data()`: Prompts for student profiles and collects scores interactively.
- `grade(average)`: Evaluates and matches numeric ranges to their structural letter grades.
- `calculate(...)`: Orchestrates the computational total, calculates the percentage, and builds the visual terminal report.

## Core Logic & Data Validation
- **Continuous Inputs**: Uses a controlled `while True` loop to allow flexible data entry until the user submits a blank line.
- **Defensive Type-Casting**: Manually converts string inputs into floating-point numbers (`float()`) to allow precise decimal evaluation.
- **Empty State Guarding**: Checks length parameters up front to prevent division-by-zero crashes if a profile contains no matching subjects.

## Concepts Practiced
- Custom Functions
- List Packing (`.append()`)
- Tuple Unpacking across function returns
- Conditional Branches (`if/elif/else`)
- Loop Controls (`while`, `break`)
- Console Layout Construction

## How to Run
Navigate to your Day-1 project directory and execute the script:
```bash
python grading_system.py
```

## Files
- `grading_system.py`: Main implementation source code file.
