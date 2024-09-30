import sqlite3, csv
from time import sleep
from Phonebook import PhoneBook
from Contacts import Contact


# main function
def main():
    try:
        phone_book = PhoneBook()
    except:
        raise RuntimeError(
            'could not initialize class "PhoneBook"! Please debug your code.'
        )

    while True:
        print("\nPhone Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Please input a number between 1-52! ").strip()

        if int(choice) < 1 or int(choice) > 6:
            raise ValueError("invalid choice. Please enter a number between 1 and 6.")

        if choice == "1":
            name = input("What name would you like to add? ")
            phonenumber = input("What is your phone number? ")
            contact = Contact(name, phonenumber)
            phone_book.add_contact(contact)
            sleep(2)

        elif choice == "2":
            phone_book.view_contacts()
            sleep(2)

        elif choice == "3":
            name = input("What name would you like to search? ")
            phone_book.search_contact(name)
            sleep(2)

        elif choice == "4":
            name = input("What name would you like to delete? ")
            phone_book.deletecontact(name)
            sleep(2)

        elif choice == "5":
            print("Exiting the phone book application.")
            break

        else:
            raise ValueError("invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
    except SyntaxError as syntaxerror:
        print(f"You have a syntax error! Here it is:\n{syntaxerror}")
    except Exception as exceptionerror:
        raise RuntimeError(f"An unexpected error has occurred: {exceptionerror}")
