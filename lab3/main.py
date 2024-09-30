from time import sleep
from Phonebook import PhoneBook
from contact import Contact


# main function
def main():
    try:
        # instance of PhoneBook
        phone_book = PhoneBook()
    except:
        # runtime error, meaning if it takes too long or doesn't initialize
        raise RuntimeError(
            'could not initialize class "PhoneBook"! Please debug your code.'
        )
    while True:
        # opening menu for number selection
        print("\nPhone Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        # input a number
        choice = input("Please input a number between 1-5! ").strip()
        # if choice is not between 1 and 5
        if int(choice) < 1 or int(choice) > 5:
            raise ValueError("invalid choice. Please enter a number between 1 and 5.")
        # choice 1 logic
        if choice == "1":
            name = input("What name would you like to add? ")
            phone_number = input("What is your phone number? ")
            contact = Contact(name, phone_number)
            phone_book.add_contact(contact)
            sleep(2)
        # chocie 2 logic
        elif choice == "2":
            phone_book.view_contacts()
            sleep(2)
        # choice 3 logic
        elif choice == "3":
            name = input("What name would you like to search? ")
            phone_book.search_contact(name)
            sleep(2)
        # choice 4 logic
        elif choice == "4":
            name = input("What name would you like to delete? ")
            phone_book.delete_contact(name)
            sleep(2)
        # chocie 5 logic
        elif choice == "5":
            print("Exiting the phone book application.")
            break


if __name__ == "__main__":
    try:
        # run main
        main()
    # raise syntax error if user does not code properlly with our class
    except SyntaxError as syntaxerror:
        print(f"You have a syntax error! Here it is:\n{syntaxerror}")
    # raise exception is something wild happens
    except Exception as exceptionerror:
        raise RuntimeError(f"An unexpected error has occurred: {exceptionerror}")
