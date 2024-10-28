from databases import *
import os


def insert_random_employees(db_name: str, num_entries: int) -> None:
    fake = Faker()
    conn: Connection = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for _ in range(num_entries):
        # Generate a unique Employee_ID
        while True:
            employee_id = random.randint(111111, 999999)
            cursor.execute(
                "SELECT COUNT(*) FROM Employee_Login WHERE Employee_ID = ?",
                (employee_id,),
            )
            if cursor.fetchone()[0] == 0:  # Check if ID does not exist
                break  # Break the loop if we found a unique ID

        first_name = fake.first_name()
        last_name = fake.last_name()
        password = fake.password()
        phone_number = fake.phone_number()
        email_address = fake.email()

        cursor.execute(
            """
            INSERT INTO Employee_Login (Employee_ID, First_Name, Last_Name, Password, Phone_Number, Email_Address)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (employee_id, first_name, last_name, password, phone_number, email_address),
        )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"{num_entries} random employee entries added!")


def print_database_contents(db_name: str) -> None:
    conn: Connection = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Print Employee_Login table
    print("Employee_Login:")
    cursor.execute("SELECT * FROM Employee_Login")
    for row in cursor.fetchall():
        print(row)

    # Print Property table
    print("\nProperty:")
    cursor.execute("SELECT * FROM Property")
    for row in cursor.fetchall():
        print(row)

    # Print Permissions table
    print("\nPermissions:")
    cursor.execute("SELECT * FROM Permissions")
    for row in cursor.fetchall():
        print(row)

    # Print Projects table
    print("\nProjects:")
    cursor.execute("SELECT * FROM Projects")
    for row in cursor.fetchall():
        print(row)

    # Print Project_Assignments table
    print("\nProject_Assignments:")
    cursor.execute("SELECT * FROM Project_Assignments")
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    db_name = os.path.join(os.getcwd(), "FindMyProperty.db")
    create_tables(db_name)
    # insert_random_employees(db_name, 2000)
    print_database_contents(db_name)  # Add this line to print the contents
