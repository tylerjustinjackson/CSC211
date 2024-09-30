import sqlite3, csv
from time import sleep


# class for contact
class Contact:
    # init class
    def __init__(self, name, phonenumber):
        if not name:
            raise ValueError("name and phone number cannot be empty.")
        if not not phonenumber:
            raise ValueError("name and phone number cannot be empty.")
        self.name = name
        self.phonenumber = phonenumber

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


if __name__ == "__main__":
    print(
        "You are running PhoneBookModule.py, please import this module to a different python files for further use."
    )
