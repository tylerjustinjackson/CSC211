import sqlite3, csv
from time import sleep


# class for contact
class Contact:
    # init class
    def __init__(self, name, phonenumber):
        # if not name:
        #     raise ValueError("name and phone number cannot be empty.")
        # if not not phonenumber:
        #     raise ValueError("name and phone number cannot be empty.")
        self.name = name
        self.phonenumber = phonenumber
        print(self.name, self.phonenumber)

    def __str__(self):
        return "Name: " + self.name + ", Phone Number: " + self.phonenumber


# phone book class
class PhoneBook:
    # init
    def __init__(self):
        self.contacts = []
        self.initdb()
        self.loadcontacts()

    # setup database
    def initdb(self):
        self.conn = sqlite3.connect("phonebook.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                name TEXT NOT NULL,
                phonenumber TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    # add contacts
    def add_contact(self, contact):
        if type(contact) != Contact:
            raise TypeError("only Contact objects can be added.")

        self.contacts.append(contact)
        self.cursor.execute(
            "INSERT INTO contacts (name, phonenumber) VALUES (?, ?)",
            (contact.name, contact.phonenumber),
        )
        self.conn.commit()
        print("Contact " + contact.name + " added successfully.")
        self.export()

    # view all contacts
    def view_contacts(self):
        if self.contacts == []:
            print("no contacts available.")
            return

        for contact in self.contacts:
            print(contact)

    # search contacts
    def search_contact(self, name):
        if type(name) != str:
            raise TypeError("name must be a string.")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return

        raise ValueError("contact with name " + name + " not found.")

    # delete contacts
    def deletecontact(self, name):
        if type(name) != str:
            raise TypeError("name must be a string.")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
                self.conn.commit()
                print("Contact " + name + " deleted successfully.")
                return
        raise ValueError("contact with name " + name + " not found.")

    # load contacts from the database
    def loadcontacts(self):
        self.cursor.execute("SELECT name, phonenumber FROM contacts")
        rows = self.cursor.fetchall()
        for row in rows:
            contact = Contact(row[0], row[1])
            self.contacts.append(contact)

    # export contacts to CSV
    def export(self, filename="contacts.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone Number"])
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phonenumber])
        print(f"Contacts exported to {filename} successfully.")


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

        choice = input("Please input a number between 1-6! ").strip()

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
