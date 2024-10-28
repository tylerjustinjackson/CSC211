import sqlite3
from sqlite3 import Connection
import re
import bcrypt


def get_employee_details() -> dict:
    """Prompts the user for employee login details and returns them as a dictionary."""
    employee_details = {}

    print("Please enter the following details for Employee Login:")

    # Prompt for Employee ID
    while True:
        employee_id = input(
            "Enter Employee ID (must be a 6-digit number starting from 111111): "
        )
        if employee_id.isdigit() and 111111 <= int(employee_id) < 1000000:
            employee_details["Employee_ID"] = int(employee_id)
            break
        else:
            print(
                "Invalid Employee ID. Please ensure it is a 6-digit number starting from 111111."
            )

    # Prompt for First Name
    employee_details["First_Name"] = input("Enter First Name: ").strip()

    # Prompt for Last Name
    employee_details["Last_Name"] = input("Enter Last Name: ").strip()

    # Prompt for Password
    while True:
        password = input(
            "Enter Password (default is your birthday in YYYY-MM-DD format): "
        )
        if re.match(r"^\d{4}-\d{2}-\d{2}$", password):  # Check for YYYY-MM-DD format
            employee_details["Password"] = (
                password  # Store password as-is for hashing later
            )
            break
        else:
            print("Invalid password format. Please enter in YYYY-MM-DD format.")

    # Prompt for Phone Number (optional)
    phone_number = input(
        "Enter Phone Number (optional, format: XXX-XXX-XXXX): "
    ).strip()
    if phone_number:  # Validate if provided
        if re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number):
            employee_details["Phone_Number"] = phone_number
        else:
            print("Invalid phone number format. It should be XXX-XXX-XXXX.")
            employee_details["Phone_Number"] = None
    else:
        employee_details["Phone_Number"] = None

    # Prompt for Email Address (optional)
    email_address = input("Enter Email Address (optional): ").strip()
    if email_address:  # Validate if provided
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email_address):
            employee_details["Email_Address"] = email_address
        else:
            print("Invalid email address format.")
            employee_details["Email_Address"] = None
    else:
        employee_details["Email_Address"] = None

    return employee_details


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def insert_employee(db_name: str, employee_details: dict) -> None:
    """Inserts the employee details into the database with a hashed password."""
    conn: Connection = sqlite3.connect(db_name)
    cursor = conn.cursor()

    hashed_password = hash_password(employee_details["Password"])

    cursor.execute(
        """
    INSERT INTO Employee_Login (
        Employee_ID,
        First_Name,
        Last_Name,
        Password,
        Phone_Number,
        Email_Address
    ) VALUES (?, ?, ?, ?, ?, ?)
    """,
        (
            employee_details["Employee_ID"],
            employee_details["First_Name"],
            employee_details["Last_Name"],
            hashed_password,  # Store the hashed password
            employee_details["Phone_Number"],
            employee_details["Email_Address"],
        ),
    )

    conn.commit()
    conn.close()
    print("Employee details successfully inserted into the database!")


def verify_password(hashed: bytes, password: str) -> bool:
    """Verifies a password against its hashed version."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


if __name__ == "__main__":
    db_name = "FindMyProperty.db"
    employee_info = get_employee_details()
    insert_employee(db_name, employee_info)

    # Example of password verification
    # (You can remove this part in a real application)
    test_password = input("Enter a password to verify: ")
    # Retrieve the hashed password from the database to verify (example)
    # For demonstration, this is a placeholder; you would normally fetch this from the database.
    hashed_password_example = hash_password(
        employee_info["Password"]
    )  # Simulating the stored hash

    if verify_password(hashed_password_example, test_password):
        print("Password verification successful!")
    else:
        print("Password verification failed.")
