import sqlite3
from sqlite3 import Connection


def get_property_details() -> dict:
    """Prompts the user for property details and returns them as a dictionary."""
    property_details = {}

    print("Please enter the following details for the Property:")

    # Prompt for Property ID
    while True:
        property_id = input(
            "Enter Property ID (must be a 6-digit number starting from 111111): "
        )
        if property_id.isdigit() and 111111 <= int(property_id) < 1000000:
            property_details["Property_ID"] = int(property_id)
            break
        else:
            print(
                "Invalid Property ID. Please ensure it is a 6-digit number starting from 111111."
            )

    # Prompt for Project ID
    property_details["Project_ID"] = input("Enter Project ID (must be a valid ID): ")

    # Prompt for Employee ID
    property_details["Employee_ID"] = input("Enter Employee ID (must be a valid ID): ")

    # Prompt for Property Type
    property_types = ["Laptop", "Desktop", "Tablet", "Phone", "Monitor", "Other"]
    print("Select Property Type:")
    for i, ptype in enumerate(property_types, 1):
        print(f"{i}. {ptype}")
    while True:
        choice = input("Enter the number corresponding to the Property Type: ")
        if choice.isdigit() and 1 <= int(choice) <= len(property_types):
            property_details["Property_Type"] = property_types[int(choice) - 1]
            break
        else:
            print("Invalid choice. Please select a valid Property Type.")

    # Prompt for Manufacturer
    property_details["Manufacturer"] = input("Enter Property Manufacturer: ")

    # Prompt for Year Manufactured
    while True:
        year_manufactured = input("Enter Year Manufactured (YYYY): ")
        if year_manufactured.isdigit() and 1900 <= int(year_manufactured) <= 2023:
            property_details["Year_Manufactured"] = int(year_manufactured)
            break
        else:
            print("Invalid year. Please enter a valid year between 1900 and 2023.")

    # Prompt for Purchase Date
    property_details["Purchase_Date"] = input("Enter Purchase Date (YYYY-MM-DD): ")

    # Prompt for MSRP
    while True:
        msrp = input("Enter MSRP (Manufacturer's Suggested Retail Price): ")
        try:
            property_details["MSRP"] = float(msrp)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for MSRP.")

    # Prompt for Last Maintenance Date
    property_details["Last_Maintenance_Date"] = input(
        "Enter Last Maintenance Date (YYYY-MM-DD): "
    )

    # Prompt for Decommissioned status
    while True:
        decommissioned = (
            input("Is the property decommissioned? (yes/no): ").strip().lower()
        )
        if decommissioned in ["yes", "no"]:
            property_details["Decommissioned"] = decommissioned == "yes"
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # If decommissioned, prompt for Decommission Date
    if property_details["Decommissioned"]:
        property_details["Decommission_Date"] = input(
            "Enter Decommission Date (YYYY-MM-DD): "
        )
    else:
        property_details["Decommission_Date"] = None

    return property_details


def insert_property(db_name: str, property_details: dict) -> None:
    """Inserts the property details into the database."""
    conn: Connection = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO Property (
        Property_ID,
        Project_ID,
        Employee_ID,
        Property_Type,
        Manufacturer,
        Year_Manufactured,
        Purchase_Date,
        MSRP,
        Last_Maintenance_Date,
        Decommissioned,
        Decommission_Date
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            property_details["Property_ID"],
            property_details["Project_ID"],
            property_details["Employee_ID"],
            property_details["Property_Type"],
            property_details["Manufacturer"],
            property_details["Year_Manufactured"],
            property_details["Purchase_Date"],
            property_details["MSRP"],
            property_details["Last_Maintenance_Date"],
            property_details["Decommissioned"],
            property_details["Decommission_Date"],
        ),
    )

    conn.commit()
    conn.close()
    print("Property details successfully inserted into the database!")


if __name__ == "__main__":
    db_name = "company_database.db"
    property_info = get_property_details()
    insert_property(db_name, property_info)
