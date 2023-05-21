from contact_database import ContactDatabase
from file_settings import FileSettings
from contact_record import ContactRecord

def main():
    # Create a ContactDatabase instance with file settings
    settings = FileSettings()
    contact_database = ContactDatabase(settings)

    # Menu-driven user interface
    choice = -1

    while choice != 0:
        print("----- Contact Database Menu -----")
        print("1. Read a record")
        print("2. Add a record")
        print("3. Delete a record")
        print("4. Search a record")
        print("5. Modify a record")
        print("6. Print all records")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Read a record
            # ...

        elif choice == 2:
            # Add a record
            # ...

        elif choice == 3:
            # Delete a record
            # ...

        elif choice == 4:
            # Search a record
            # ...

        elif choice == 5:
            # Modify a record
            # ...

        elif choice == 6:
            # Print all records
            contact_database.print_all_records()

        elif choice == 0:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
