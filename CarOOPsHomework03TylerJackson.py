# Making vehicle class
class Vehicle:

    # Inititialize vehicle class and attributes
    def __init__(self):
        self.category = "vehicle"

        # prints attribute of for any subclasses
        def type(self) -> print:
            print(f"This is model falls under the {self.category} type!")


# Makes car subclass from Vehicle class
class Car(Vehicle):

    category = Vehicle.category

    # Initializer for instance and attributes
    def __init__(self, model: str, color: str, year: int, manufacturer: str):
        self.model = model
        self.color = color
        self.year = year
        self.manufacturer = manufacturer

    # Creates instance method for description
    def description(self) -> str:
        return f"The car is a {self.color} {self.model} made in {self.year} by {self.manufacturer}."

    # Creates another instance method for vehicle type
    def typeofcar(self, car_type: str) -> str:
        return f"This {self.model} a {car_type}."


if __name__ == "__main__":

    try:
        # Creating an object
        my_car = Car("Veloster", "White", 2013, "Hyundai")

        # getting attributes and methods
        print(my_car.description())  # The car is a Hyundai Veloster from 2013.
        print(my_car.typeofcar("Commuter Car"))  # This is a Commuter Car for school.

    # Error handling
    except SyntaxError as se:
        print(se)
    except:
        print("Model Failed to Load")
