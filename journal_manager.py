import os
from datetime import datetime


# ============================================================
# MAIN MENU
# ============================================================

def main():
    journal = JournalManager()

    while True:
        print("\n" + "=" * 45)
        print("Welcome to Personal Journal Manager!")
        print("=" * 45)

        print("\nPlease select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            journal.add_entry()

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_all_entries()

        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid option. Please select a valid option from the menu.")


# ============================================================
# JOURNAL MANAGER CLASS
# ============================================================

class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # --------------------------------------------------------
    # ADD A NEW ENTRY
    # --------------------------------------------------------
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ").strip()

            if not entry:
                print("Journal entry cannot be empty.")
                return

            if not os.path.exists(self.filename):
                try:
                    with open(self.filename, "x"):
                        pass
                except FileExistsError:
                    pass

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while accessing the journal file.")

        except OSError as error:
            print(f"File error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")

    # --------------------------------------------------------
    # VIEW ALL ENTRIES
    # --------------------------------------------------------
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if not content.strip():
                print("\nNo journal entries found.")
                return

            print("\nYour Journal Entries:")
            print("-" * 40)
            print(content)

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied while reading the journal file.")

        except OSError as error:
            print(f"File error: {error}")

    # --------------------------------------------------------
    # SEARCH FOR AN ENTRY
    # --------------------------------------------------------
    def search_entry(self):
        try:
            keyword = input(
                "\nEnter a keyword or date to search: "
            ).strip()

            if not keyword:
                print("Search keyword cannot be empty.")
                return

            with open(self.filename, "r") as file:
                lines = file.readlines()

            matches = []
            current_entry = []

            for line in lines:
                if line.strip() == "-" * 40:
                    entry_text = "".join(current_entry)

                    if keyword.lower() in entry_text.lower():
                        matches.append(entry_text)

                    current_entry = []
                else:
                    current_entry.append(line)

            if current_entry:
                entry_text = "".join(current_entry)

                if keyword.lower() in entry_text.lower():
                    matches.append(entry_text)

            if matches:
                print("\nMatching Entries:")
                print("-" * 40)

                for entry in matches:
                    print(entry)

            else:
                print(
                    f"\nNo entries were found for the keyword: {keyword}."
                )

        except FileNotFoundError:
            print(
                "\nError: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("Error: Permission denied while searching the journal file.")

        except OSError as error:
            print(f"File error: {error}")

    # --------------------------------------------------------
    # DELETE ALL ENTRIES
    # --------------------------------------------------------
    def delete_all_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().lower()

            if confirmation != "yes":
                print("\nDeletion cancelled.")
                return

            with open(self.filename, "w") as file:
                file.write("")

            os.remove(self.filename)

            print("\nAll journal entries have been deleted.")

        except FileNotFoundError:
            print("\nNo journal entries to delete.")

        except PermissionError:
            print("Error: Permission denied while deleting the journal.")

        except OSError as error:
            print(f"File error: {error}")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()