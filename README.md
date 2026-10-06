# File Operator – Personal Journal Manager

## 📌 Project Overview

**File Operator – Personal Journal Manager** is a menu-driven Python application developed to manage personal journal entries using **Object-Oriented Programming (OOP)** and **file handling**.

The application allows users to create, view, search, and delete journal entries through a simple command-line menu. Journal entries are stored in a text file, making the data easy to save and retrieve without using a database.

This project demonstrates the practical use of Python concepts such as:

- Classes and Objects
- Constructors
- Methods
- File Handling
- Different File Modes
- Exception Handling
- Conditional Statements
- Loops
- User Input
- Date and Time Handling

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To develop a simple personal journal management system using Python.
2. To understand and implement Object-Oriented Programming concepts.
3. To practice reading and writing data using text files.
4. To use different file modes such as `r`, `w`, `a`, and `x`.
5. To implement exception handling for file-related errors.
6. To create a user-friendly menu-driven command-line application.
7. To store journal entries with date and time information.
8. To provide search functionality for previously stored entries.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Text File (`.txt`) | Storage of journal entries |
| OOP | Program structure using classes and objects |
| File Handling | Reading, writing, appending, and creating files |
| Exception Handling | Handling runtime and file-related errors |
| `datetime` Module | Adding date and time to journal entries |
| `os` Module | Checking and managing the journal file |

## File Description
journal_manager.py

This is the main Python program. It contains the menu, JournalManager class, and all the operations required to manage journal entries.

journal.txt

This file is created automatically by the program when the user adds the first journal entry.

It is used to store the journal data.

## 🚀 Features
1. Add a New Entry

The user can enter a new personal journal entry.

The program automatically adds the current date and time to the entry and stores it in the journal file.

2. View All Entries

This option reads the journal file and displays all previously saved entries.

The program informs the user if:

The journal file does not exist.
No entries are available.
The file cannot be accessed.

3. Search for an Entry

The user can search for a journal entry using:

A keyword
A word or phrase
A date

The program checks the stored entries and displays matching results.

4. Delete All Entries

This option allows the user to remove all stored journal entries.

Before deleting the data, the program asks for confirmation:

Are you sure you want to delete all entries? (yes/no):

The entries are deleted only when the user enters:

yes

This prevents accidental deletion.

5. Exit

The user can select the Exit option to close the application.

Thank you for using Personal Journal Manager. Goodbye!

## 📋 Main Menu

When the program starts, the main menu is displayed first.

Welcome to Personal Journal Manager!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter your choice:

The user selects an option and the corresponding operation is performed.

After completing the operation, the program returns to the main menu.

## 🧱 OOP Implementation

The project uses a class named:

class JournalManager:

An object of this class is created in the main() function:

journal = JournalManager()

The class contains methods for the different operations of the application.

Constructor
def __init__(self, filename="journal.txt"):
    self.filename = filename

The constructor initializes the name of the file used for storing journal entries.

## 🔧 Class Methods

### add_entry()

Adds a new journal entry to the text file.

It uses append mode so that existing entries are preserved.

with open(self.filename, "a") as file:

### view_entries()

Reads and displays all stored journal entries.

It uses read mode:

with open(self.filename, "r") as file:

### search_entry()

Searches for a keyword or date inside the stored journal entries.

The search is case-insensitive, making it easier for the user to find information.

### delete_all_entries()

Removes all journal data after asking for user confirmation.

Write mode is used to clear the file before the file is removed.

with open(self.filename, "w") as file:
    file.write("")
## 📁 File Handling

File handling is one of the main concepts demonstrated in this project.

### r – Read Mode

Used to read existing journal entries.

open(self.filename, "r")
### a – Append Mode

Used to add new entries without removing existing entries.

open(self.filename, "a")
### w – Write Mode

Used to clear the contents of the file.

open(self.filename, "w")
### x – Create Mode

Used to create the journal file when it does not already exist.

open(self.filename, "x")
## 🛡️ Exception Handling

The project uses exception handling to make the application more reliable.

The following exceptions are handled:

FileNotFoundError

Occurs when the journal file does not exist while trying to read or search it.

Example:

Error: The journal file does not exist.
Please add a new entry first.
PermissionError

Handles situations where the program does not have permission to access the file.

Example:

Error: Permission denied while accessing the journal file.
OSError

Handles other file-system-related errors.

Example:

File error: ...
General Exception

Unexpected errors are also handled during the add operation to prevent the program from terminating unexpectedly.

## ⏰ Date and Time

The project uses Python's datetime module to automatically store the date and time of each journal entry.

This provides a record of when each journal entry was created.

## ✅ Advantages
- Simple and easy-to-use command-line interface
- No database required
- Journal data is stored permanently in a text file
- New entries can be added without deleting old entries
- Entries can be searched using keywords
- Date and time are stored automatically
- Handles common file errors
- Demonstrates practical Python and OOP concepts

## ⚠️ Limitations
- The application works through the command line only.
- Data is stored in a text file instead of a database.
- There is no user authentication.
- Entries cannot be edited individually.
- Deleting all entries removes all stored journal data.

## 🔮 Future Improvements

The project can be enhanced in the future by adding:

- Edit or update individual entries
- Delete a single selected entry
- User login and authentication
- Graphical User Interface (GUI)
- Database storage
- Categories or tags for journal entries
- Export journal entries to PDF
- Password protection
- Improved search and filtering

## 🎓 Learning Outcome

Through this project, I learned how to:

- Build a menu-driven Python application.
- Design a program using Object-Oriented Programming.
- Create and use classes and objects.
- Work with text files in Python.
- Use different file modes such as r, w, a, and x.
- Handle file-related exceptions.
- Store date and time with user data.
- Implement searching and deletion functionality.
- Create a complete Python project suitable for practical submission.

## 📸 Project Screenshots

Screenshots of the program execution can be added here.

Example:

![Main Menu](screenshots/main_menu.png)

![Add Entry](screenshots/add_entry.png)

![View Entries](screenshots/view_entries.png)

![Search Entry](screenshots/search_entry.png)

![Delete Entries](screenshots/delete_entries.png)

## ✅ Conclusion

The **File Operator – Personal Journal Manager** is a simple and practical Python application that successfully demonstrates Object-Oriented Programming, file handling, and exception handling.

The project provides an easy way to add, view, search, and delete personal journal entries using a text file. It also records the date and time of each entry and handles common file-related errors.

By developing this project, I gained practical knowledge of Python classes and objects, file modes, exception handling, loops, conditions, functions, and date-time operations.

Overall, this project helped me understand how Python concepts can be combined to develop a complete menu-driven application. The project can be extended in the future with features such as editing individual entries, deleting selected entries, user authentication, GUI support, and database integration.
