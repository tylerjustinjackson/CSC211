# class for contact
class Contact:
    # init class
    def __init__(self, name, phone_number):
        # name and number assignment
        if not name or not phone_number:
            raise ValueError("name and phone number cannot be empty.")
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        # print info for screen
        return "Name: " + self.name + ", Phone Number: " + self.phone_number
