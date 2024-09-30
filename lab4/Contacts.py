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
