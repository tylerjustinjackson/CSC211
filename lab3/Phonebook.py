from contact import Contact


# phone book class
class PhoneBook(Contact):
    # init
    def __init__(self):
        self.contacts = []
        if not isinstance(self.contacts, list):
            raise TypeError("contacts should be stored in a list.")

    # add contacts
    def add_contact(self, contact):
        if not isinstance(contact, Contact):
            raise TypeError("only Contact objects can be added.")

        self.contacts.append(contact)
        print("Contact " + contact.name + " added successfully.")

    # view all contacts
    def view_contacts(self):
        if self.contacts == []:
            print("no contacts available.")
            return
        # print all contacts
        for contact in self.contacts:
            print(contact)

    # search contacts
    def search_contact(self, name):
        # must have a string name
        if not isinstance(name, str):
            raise TypeError("name must be a string.")
        # loop through all contacts
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        # value error if contact is not found
        raise ValueError("contact with name " + name + " not found.")

    # delete contacts
    def delete_contact(self, name):
        # contact must be a string, raise TyperError
        if not isinstance(name, str):
            raise TypeError("name must be a string.")
        # loop through all contacts and delete them
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact " + name + " deleted successfully.")
                return
        # if contact not found raise a Value error
        raise ValueError("contact with name " + name + " not found.")
