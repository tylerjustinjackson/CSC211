# class for contact
class Contact:
    # init class
    def __init__(self, name: str, phonenumber: str) -> None:
        self.name: str = name
        self.phonenumber: str = phonenumber
        # print(self.name, self.phonenumber)

    def __str__(self) -> str:
        return "Name: " + self.name + ", Phone Number: " + self.phonenumber
