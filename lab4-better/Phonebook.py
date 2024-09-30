from Contacts import Contact
import sqlite3


# phone book class
class PhoneBook:
    # init
    def __init__(self) -> None:
        self.contacts: list[Contact] = []
        self.initdb()
        self.loadcontacts()

    # setup database
    def initdb(self) -> None:
        self.conn: sqlite3.Connection = sqlite3.connect("phonebook.db")
        self.cursor: sqlite3.Cursor = self.conn.cursor()
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
    def add_contact(self, contact: Contact) -> None:
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
    def view_contacts(self) -> None:
        if self.contacts == []:
            print("no contacts available.")
            return

        for contact in self.contacts:
            print(contact)

    # search contacts
    def search_contact(self, name: str) -> None:
        if type(name) != str:
            raise TypeError("name must be a string.")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return

        raise ValueError("contact with name " + name + " not found.")

    # delete contacts
    def deletecontact(self, name: str) -> None:
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
    def loadcontacts(self) -> None:
        self.cursor.execute("SELECT name, phonenumber FROM contacts")
        rows = self.cursor.fetchall()
        for row in rows:
            contact = Contact(row[0], row[1])
            self.contacts.append(contact)
