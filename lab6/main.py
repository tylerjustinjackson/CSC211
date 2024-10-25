from time import sleep
from Phonebook import PhoneBook
from Contacts import Contact
from report import generate_report, printreport


def choice_1(phone_book: PhoneBook) -> None:
    name: str = input("What name would you like to add? ")
    phonenumber: str = input("What is your phone number? ")
    contact: Contact = Contact(name, phonenumber)
    phone_book.add_contact(contact)
    sleep(2)


def choice_2(phone_book: PhoneBook) -> None:
    phone_book.view_contacts()
    sleep(2)


def choice_3(phone_book: PhoneBook) -> PhoneBook:
    while True:
        try:
            name: str = input("What name would you like to search? ")
            phone_book.search_contact(name)
            sleep(2)
            break

        except ValueError:
            print("Please input a valid contact")


def choice_4(phone_book: PhoneBook) -> None:
    while True:
        try:
            name: str = input("What name would you like to delete? ")
            phone_book.deletecontact(name)
            sleep(2)
            break

        except ValueError:
            print("Please input a valid contact name")


def choice_5() -> None:
    print("Exiting the phone book application.\nGenerating report now")
    for i in range(1, 4):
        print("." * i)
        sleep(1)


# main function
def main() -> None:
    try:
        phone_book: PhoneBook = PhoneBook()
    except:
        raise RuntimeError(
            'could not initialize class "PhoneBook"! Please debug your code.'
        )

    while True:
        print("\nPhone Book Application:\nMenu:\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit and Generate Report\n")

        choice: str = input("Please input a number between 1-5! ").strip()
        print()

        try:
            if int(choice) < 1 or int(choice) > 6:
                raise ValueError(
                    "invalid choice. Please enter a number between 1 and 6."
                )

        except ValueError:
            print("Please input a valid choice as an integer 1-5")

        if choice == "1":
            choice_1(phone_book)

        elif choice == "2":
            choice_2(phone_book)

        elif choice == "3":
            choice_3(phone_book)

        elif choice == "4":
            choice_4(phone_book)

        elif choice == "5":
            choice_5()
            break

        else:
            raise ValueError("invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
        generate_report()
        printreport()
    except SyntaxError as syntaxerror:
        print(f"You have a syntax error! Here it is:\n{syntaxerror}")
    except Exception as exceptionerror:
        raise RuntimeError(f"An unexpected error has occurred: {exceptionerror}")
