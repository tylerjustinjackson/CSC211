import sqlite3
from sqlite3 import Connection


def create_tables(db_name: str) -> None:

    conn: Connection = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create Employee Login table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Employee_Login (
        Employee_ID INTEGER PRIMARY KEY,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        Password TEXT NOT NULL,
        Phone_Number TEXT,
        Email_Address TEXT
    )
    """
    )

    # Create Property table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Property (
        Property_ID INTEGER PRIMARY KEY,
        Project_ID INTEGER,
        Employee_ID INTEGER,
        Property_Type TEXT NOT NULL,
        Manufacturer TEXT NOT NULL,
        Year_Manufactured INTEGER,
        Purchase_Date TEXT,
        MSRP REAL,
        Last_Maintenance_Date TEXT,
        Decommissioned BOOLEAN NOT NULL,
        Decommission_Date TEXT,
        FOREIGN KEY (Employee_ID) REFERENCES Employee_Login(Employee_ID)
    )
    """
    )

    # Create Permissions table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Permissions (
        Employee_ID INTEGER PRIMARY KEY,
        Managerial_Level TEXT,
        FOREIGN KEY (Employee_ID) REFERENCES Employee_Login(Employee_ID)
    )
    """
    )

    # Create Projects table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Projects (
        Project_ID INTEGER PRIMARY KEY,
        Project_Title TEXT NOT NULL,
        Skills_Needed TEXT
    )
    """
    )

    # Create Project Assignments table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Project_Assignments (
        Project_ID INTEGER,
        Employee_ID INTEGER,
        PRIMARY KEY (Project_ID, Employee_ID),
        FOREIGN KEY (Project_ID) REFERENCES Projects(Project_ID),
        FOREIGN KEY (Employee_ID) REFERENCES Employee_Login(Employee_ID)
    )
    """
    )

    # Commit the changes and closes the connection
    conn.commit()
    conn.close()

    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables("FindMyProperty.db")