from employeelogin import *
from databases import *
from property import *
import os

if __name__ == "__main__":
    db_name = os.path.join(os.path.dirname(__file__), "FindMyProperty.db")

    # Create tables if they do not exist
    create_tables(db_name)

    # Get and insert employee details
    employee_info = get_employee_details()
    insert_employee(db_name, employee_info)

    # Get and insert property details
    property_info = get_property_details()
    insert_property(db_name, property_info)
