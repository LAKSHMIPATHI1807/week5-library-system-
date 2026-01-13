Week5 - Project Name: LIBRARY MANAGEMENT SYSTEM
A console-based Library Management System developed using Python and Object-Oriented Programming (OOP).
This project allows managing books and members, borrowing and returning books, tracking overdue items, and saving data using JSON files.

Project Objectives

Apply Object-Oriented Programming concepts
Use JSON file handling for persistent storage
Build a menu-driven CLI application
Simulate real-world library operations
Write clean, modular, and testable code

Project Structure

week5-library-system/
│── library_system/
│   ├── __init__.py
│   ├── book.py        # Book class with loan & overdue logic
│   ├── member.py      # Member class with borrow limits
│   ├── library.py     # Core library operations
│   └── main.py        # Menu-driven interface
│
│── data/
│   ├── books.json     # Stores book records
│   ├── members.json   # Stores member records
│   └── backup/        # Backup files
│
│── tests/
│   ├── test_book.py
│   ├── test_member.py
│   └── test_library.py
│
│── requirements.txt
│── README.md
└── .gitignore

Features
Book Management

Add new books

View all books

Search books by title, author, or ISBN
Track availability status
Member Management
Register new members
View all members
Enforce borrow limit (maximum 5 books)

Borrow & Return
Borrow books with automatic due date (14 days)
Return borrowed books
Update availability status

Overdue Tracking

View overdue books
Show days overdue
Display borrower details
Data Persistence
Save books and members to JSON files
Load data automatically on program start
Save data before exit

Module Description

book.py
Handles all book-related operations.

Attributes:
title, author, isbn, year
available, borrowed_by, due_date, date_added

Methods:
check_out()
return_book()
is_overdue()
days_overdue()
to_dict() / from_dict()

member.py
Handles member information and borrow limits.

Attributes:
name
member_id
borrowed_books

Methods:
borrow_book()
return_book()

library.py
Central management class.

Responsibilities:
Manage books and members
Borrow and return operations
View all books, members, overdue books
Save and load data from JSON files

main.py

Entry point of the application.
Displays menu options
Accepts user input
Calls library functions
Saves data on exit

How to Run the Project
Install Python 3.8 or higher
Open terminal in project directory

Run the application:
python library_system/main.py

Running Unit Tests
python -m unittest discover tests

Requirements
Python 3.8+
(No external libraries required)

Learning Outcomes

Strong understanding of OOP in Python
File handling using JSON
Date and overdue calculations
Menu-driven program design
Writing unit tests
Modular project structure

Future Enhancements

Fine calculation for overdue books
Role-based access (Admin / User)
GUI or Web-based interface
Email/SMS notifications
Report generation (CSV / PDF)
